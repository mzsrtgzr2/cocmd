#!/usr/bin/env bash

# Copyright 2018- The ggist Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

################################################################
# ggist Installer
# This is inspired by the homebrew installer.
################################################################
set -u

CLOUD_ADDR=${PL_CLOUD_ADDR:-"ggist.io"}
DEFAULT_INSTALL_PATH=/usr/local/bin
ARTIFACT_NAME=cli_darwin_universal
USE_VERSION=${PL_CLI_VERSION:-latest}
USER_INSTALL_PATH="$HOME/bin"
ARTIFACT_BUCKET="ggist-dev-public"
if [[ $USE_VERSION == *"-"* ]]; then
  ARTIFACT_BUCKET="ggist-prod-artifacts"
fi
ARTIFACT_BASE_PATH="https://storage.googleapis.com/${ARTIFACT_BUCKET}/cli"


ggist_BANNER="

 ██████╗  ██████╗ ██╗███████╗████████╗
██╔════╝ ██╔════╝ ██║██╔════╝╚══██╔══╝
██║  ███╗██║  ███╗██║███████╗   ██║   
██║   ██║██║   ██║██║╚════██║   ██║   
╚██████╔╝╚██████╔╝██║███████║   ██║   
 ╚═════╝  ╚═════╝ ╚═╝╚══════╝   ╚═╝                        
"

# Check if the OS is Linux.
if [[ "$(uname)" = "Linux" ]]; then
    ARTIFACT_NAME=cli_linux_amd64
fi

# String formatting functions.
if [[ -t 1 ]]; then
  tty_escape() { printf "\033[%sm" "$1"; }
else
  tty_escape() { :; }
fi

tty_mkbold() { tty_escape "1;$1"; }
tty_underline="$(tty_escape "4;39")"
tty_cyan="$(tty_mkbold 36)"
tty_yellow="$(tty_mkbold 33)"
tty_green="$(tty_mkbold 32)"
tty_red="$(tty_mkbold 31)"
tty_bold="$(tty_mkbold 39)"
tty_reset="$(tty_escape 0)"

# Trap ctrl-c and call ctrl_c() to reset terminal.
trap ctrl_c INT

function ctrl_c() {
    stty sane
    exit
}

# Parse Options:
#TODO(zasgar): Better usage.
usage() {
    cat << EOS

${tty_bold}Usage:${tty_reset} $0

EOS
    exit 1
}

while getopts ":v:c:h" o; do
    case "${o}" in
        h)
            usage
            ;;
        *)
            usage
            ;;
    esac
done
shift $((OPTIND-1))

print_dev_message() {
  if [[ -n "${PL_TESTING_ENV:-}" ]]; then
    emph_red "${tty_red}IN DEVELOPMENT MODE: PL_TESTING_ENV=${PL_TESTING_ENV},"\
              "PL_CLI_VERSION=${PL_CLI_VERSION:-}, PL_VIZIER_VERSION=${PL_VIZIER_VERSION:-}"\
              "PL_CLOUD_ADDR=${PL_CLOUD_ADDR:-}${tty_reset}"
  fi
}

artifact_url() {
  echo "${ARTIFACT_BASE_PATH}/${USE_VERSION}/${ARTIFACT_NAME}"
}

have_sudo_access() {
  if [[ -z "${HAVE_SUDO_ACCESS-}" ]]; then
    /usr/bin/sudo -l mkdir &>/dev/null
    HAVE_SUDO_ACCESS="$?"
  fi

  return "$HAVE_SUDO_ACCESS"
}

shell_join() {
  local arg
  printf "%s" "$1"
  shift
  for arg in "$@"; do
    printf " "
    printf "%s" "${arg// /\ }"
  done
}

emph_red() {
  printf "${tty_red}==>${tty_bold} %s${tty_reset}\n" "$(shell_join "$@")"
}

emph() {
  printf "${tty_cyan}==>${tty_bold} %s${tty_reset}\n" "$(shell_join "$@")"
}

abort() {
  printf "%s\n" "$1"
  exit 1
}

execute() {
  if ! "$@"; then
    abort "$(printf "Failed during: %s" "$(shell_join "$@")")"
  fi
}

wait_for_user() {
  local c
  echo
  read -r -p "Continue (Y/n): " c
  # We test for \r and \n because some stuff does \r instead.
  if ! [[ "$c" == '' || "$c" == $'\r' || "$c" == $'\n' || "$c" == 'Y' || "$c" == 'y' ]]; then
    exit 1
  fi
  echo
}

exists_but_not_writable() {
  [[ -e "$1" ]] && ! [[ -r "$1" && -w "$1" && -x "$1" ]]
}

print_dev_message

if exists_but_not_writable "${DEFAULT_INSTALL_PATH}"; then
    DEFAULT_INSTALL_PATH=${USER_INSTALL_PATH}
fi

echo "${tty_green}${ggist_BANNER}${tty_reset}"

emph "Info:"
cat << EOS
ggist is a terminal utility to find and create:
- aliases
- scripts
- terminal playbooks

Docs:
  ${tty_underline}https://${CLOUD_ADDR}/docs${tty_reset}
EOS


printf "\n\n"
emph "Terms and Conditions ${tty_underline}https://www.ggistlabs.ai/terms${tty_reset}"
read -r -p "I have read and accepted the Terms & Conditions [y/n]: " READ_TERMS
printf "\n\n"

READ_TERMS=${READ_TERMS:0:1}
if ! [[ "$READ_TERMS" == 'Y' || "$READ_TERMS" == 'y' ]]; then
    abort "Cannot install GGIST CLI until you accept the Terms & Conditions."
fi

emph "Installing GGIST CLI:"
pip install ggist1 --upgrade
echo 'Installation OK'

echo 'eval "$(ggist apply)"' >> ~/.bashrc
echo 'updated bash'
echo 'eval "$(ggist apply)"' >> ~/.zshrc
echo 'updated zsh'

echo
emph "Next steps:"
cat << EOS

add aliases and goodies, for example:
- ggist add source demo/k8s
- ggist add source demo/git
- ggist add source demo/docker

run playbooks:
- ggist play flow k8s-setup
- ggist play flow awscli-setup
- ggist play flow zsh-setup

EOS
