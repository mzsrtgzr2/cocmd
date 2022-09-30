import os
import click
from ggist_cli_app.consts import Consts
from ggist_cli_app.utils.fs import mkdir, touch

class Context:
    def __init__(self, home=None, terminal=None):
        self.home = os.path.abspath(home or Consts.HOME)
        self.terminal = terminal or Consts.DEFAULT_TERMINAL
        self.aliases_file = os.path.join(self.home, Consts.ALIASES_FILE)
        self.scripts_dir = os.path.join(self.home, Consts.SCRIPTS_DIR)
        mkdir(self.home)
        touch(self.aliases_file)
        mkdir(self.scripts_dir)


# from https://click.palletsprojects.com/en/8.1.x/complex/
click_pass_context = click.make_pass_decorator(Context, ensure=True)
