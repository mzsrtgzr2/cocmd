# Hi 

**cocmd** is a terminal utility to find and create:
- aliases
- scripts


## Getting Started
The easiest way to install Cocmd's CLI is using the install script:

```
# Copy and run command to install the CLI.
bash -c "$(curl -fsSL https://raw.githubusercontent.com/mzsrtgzr2/cocmd/main/cli/install.sh)"
```


# Add new aliases and scripts
Currently only demo - 

```
cocmd add source demo/k8s
cocmd add source demo/git
cocmd add source demo/docker
cocmd add source demo/awscli
cocmd add source demo/zsh
cocmd add source demo/team1
cocmd add source demo/osx
```

### Run scripts
for example, Team1 have an onboarding script.
run it, you will be prompt to approve every step:
```
cocmd run team1.onboarding
```

to see all available scripts run `cocmd show scripts`

** Make sure you open a new terminal to see the changes **

### to see all your sources
```
cocmd show sources
```

### See all your aliases
```
cocmd show aliases
```

### See all your scripts
```
cocmd show aliases
```


## Vision 

manage your aliases and scripts
    - get new from community 
    - create your own
    - complicated installations in one command
    - synchronize in your team


## TODO:
- grafana runner - query
- jenkins runner - query