

import pprint
from ggist_cli_app.utils import io
from ggist_cli_app.core.models.script_model import *




data_onboarding = ScriptModel(
    name="onboarding",
    title="New Developer onboarding ",
    description="Welcome to the team!",
    spec=SpecModel(
        globals=[
            
        ],
        variations=[
        StepsModel(
            env=OS.LINUX,
            label="debian",
            steps=[
                StepModel(
                    title="Install docker",
                    description="This will install docker on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        # Update instance
                        sudo apt update -y
                        sudo apt upgrade -y

                        # Install docker
                        sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
                        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
                        apt-cache policy docker-ce
                        sudo apt install docker-ce -y

                        # Automatically start Docker and Containerd on boot for non debian or ubuntu distros.
                        sudo systemctl enable docker
                        sudo systemctl enable containerd.service

                        # Add possibility to call docker without sudo
                        sudo usermod -aG docker ${USER}

                        # Check is instalation successful
                        docker --version
                        """
                ),
                StepModel(
                    title="Install docker-compose",
                    description="This will install docker-compose on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                        sudo chmod +x /usr/local/bin/docker-compose
                        docker-compose version
                        """
                ),
            ]),

        StepsModel(
            env=OS.OSX,
            label=">10.x.x",
            depends=[
                "installed:brew",
            ],
            steps=[
                StepModel(
                    title="Install docker",
                    description="This will install docker on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        # Update instance
                        sudo apt update -y
                        sudo apt upgrade -y

                        # Install docker
                        sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
                        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
                        apt-cache policy docker-ce
                        sudo apt install docker-ce -y

                        # Automatically start Docker and Containerd on boot for non debian or ubuntu distros.
                        sudo systemctl enable docker
                        sudo systemctl enable containerd.service

                        # Add possibility to call docker without sudo
                        sudo usermod -aG docker ${USER}

                        # Check is instalation successful
                        docker --version
                        """
                ),
                StepModel(
                    title="Install docker-compose",
                    description="This will install docker-compose on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                        sudo chmod +x /usr/local/bin/docker-compose
                        docker-compose version
                        """
                ),
            ]),
    ])
)

io.YamlIO.to_file('/workspaces/ggist/ggist_cli_app/resources/demo/team1/scripts/onboarding.yaml', data_onboarding)


data_docker = ScriptModel(
    name="setup",
    title="Setup AwsCli ",
    description="setup docker for desktop",
    spec=SpecModel(
        globals=[
            
        ],
        variations=[
        StepsModel(
            env=OS.LINUX,
            label="debian",
            steps=[
                StepModel(
                    title="Install docker",
                    description="This will install docker on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        # Update instance
                        sudo apt update -y
                        sudo apt upgrade -y

                        # Install docker
                        sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
                        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
                        apt-cache policy docker-ce
                        sudo apt install docker-ce -y

                        # Automatically start Docker and Containerd on boot for non debian or ubuntu distros.
                        sudo systemctl enable docker
                        sudo systemctl enable containerd.service

                        # Add possibility to call docker without sudo
                        sudo usermod -aG docker ${USER}

                        # Check is instalation successful
                        docker --version
                        """
                ),
                StepModel(
                    title="Install docker-compose",
                    description="This will install docker-compose on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                        sudo chmod +x /usr/local/bin/docker-compose
                        docker-compose version
                        """
                ),
            ]),

        StepsModel(
            env=OS.OSX,
            label=">10.x.x",
            depends=[
                "installed:brew",
            ],
            steps=[
                StepModel(
                    title="Install docker",
                    description="This will install docker on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        # Update instance
                        sudo apt update -y
                        sudo apt upgrade -y

                        # Install docker
                        sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
                        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
                        sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
                        apt-cache policy docker-ce
                        sudo apt install docker-ce -y

                        # Automatically start Docker and Containerd on boot for non debian or ubuntu distros.
                        sudo systemctl enable docker
                        sudo systemctl enable containerd.service

                        # Add possibility to call docker without sudo
                        sudo usermod -aG docker ${USER}

                        # Check is instalation successful
                        docker --version
                        """
                ),
                StepModel(
                    title="Install docker-compose",
                    description="This will install docker-compose on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                        sudo chmod +x /usr/local/bin/docker-compose
                        docker-compose version
                        """
                ),
            ]),
    ])
)

io.YamlIO.to_file('/workspaces/ggist/ggist_cli_app/resources/demo/docker/scripts/setup.yaml', data_docker)


data_awscli = ScriptModel(
    name="setup",
    title="Setup AwsCli ",
    description="setup awscli for desktop",
    spec=SpecModel(
        globals=[
            
        ],
        variations=[
        StepsModel(
            env=OS.LINUX,
            label="debian",
            steps=[
                StepModel(
                    title="Install awscli",
                    description="This will install awscli on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
                        unzip awscliv2.zip
                        sudo ./aws/install
                        aws --version
                        rm -rf awscliv2.zip aws
                        """
                ),
                StepModel(
                    title="Configure Aws credentials and environment",
                    description="",
                    runner=StepRunnerType.SHELL,
                    content="""
                    aws configure
                    """
                )
            ]),

        StepsModel(
            env=OS.OSX,
            label=">10.x.x",
            depends=[
                "installed:brew",
            ],
            steps=[
                StepModel(
                    title="Install awscli",
                    description="This will install awscli on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
                        curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
                        sudo installer -pkg AWSCLIV2.pkg -target /
                        aws --version
                        rm -rf AWSCLIV2.pkg aws
                        """
                ),
                StepModel(
                    title="Configure Aws credentials and environment",
                    description="",
                    runner=StepRunnerType.SHELL,
                    content="""
                    aws configure
                    """
                )
            ]),
    ])
)

io.YamlIO.to_file('/workspaces/ggist/ggist_cli_app/resources/demo/awscli/scripts/setup.yaml', data_awscli)




data_k8s = ScriptModel(
    name="setup",
    title="Setup Kubernetes",
    description="setup Kubernetes for desktop",
    spec=SpecModel(
        globals=[
            StepGlobalModel(
                    title="Instructions",
                    description="",
                    runner=StepRunnerType.MARKDOWN,
                    content="""
# Kubernetes is awesome
## cheers
### all good
                    """,
                    id="kube_instructions_md"
                )
        ],
        variations=[
        StepsModel(
            env=OS.LINUX,
            label="debian",
            steps=[
                StepRefModel(ref="kube_instructions_md"),
                StepModel(
                    title="Install kubectl",
                    description="This will install kubectl on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""
curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"
curl -LO \"https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256\"
echo \"$(cat kubectl.sha256)  kubectl\" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
rm -rf kubectl kubectl.sha256
"""
                ),
                StepModel(
                    title="Install kubectx",
                    description="",
                    runner=StepRunnerType.SHELL,
                    content="""
                    sudo git clone https://github.com/ahmetb/kubectx /usr/local/kubectx
                    sudo ln -s /usr/local/kubectx/kubectx /usr/local/bin/kubectx
                    sudo ln -s /usr/local/kubectx/kubens /usr/local/bin/kubens
                    """
                ),
                StepModel(
                    title="Install Minikube",
                    description="",
                    runner=StepRunnerType.SHELL,
                    content="""
                    
                    sudo apt-get install -y conntrack

                    # Download minikube
                    wget https://github.com/kubernetes/minikube/releases/download/v0.24.0/minikube_0.24-0.deb

                    # Install minikube
                    sudo dpkg -i minikube_0.24-0.deb

                    rm -rf minikube_0.24-0.deb

                    # Start minikube vm-driver=none option

                    sudo minikube start --vm-driver=none

                    # Change permission
                    sudo chown -R $USER $HOME/.kube
                    sudo chgrp -R $USER $HOME/.kube
                    sudo chown -R $USER $HOME/.minikube
                    sudo chgrp -R $USER $HOME/.minikube

                    # Make sure that minikube is running
                    kubectl get pods --all-namespaces
                    """
                )
            ]),

        StepsModel(
            env=OS.OSX,
            label=">10.x.x",
            depends=[
                "installed:brew",
            ],
            steps=[
                StepModel(
                    title="Install kubectl",
                    description="This will install kubectl on your machine",
                    runner=StepRunnerType.SHELL,
                    content="""curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\"
curl -LO \"https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256\"
echo \"$(cat kubectl.sha256)  kubectl\" | sha256sum --check
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
rm -rf kubectl kubectl.sha256
"""
                ),
                StepModel(
                    title="Install kubectx",
                    description="",
                    runner=StepRunnerType.SHELL,
                    content="""brew install kubectx"""
                ),
                StepModel(
                    title="Install Minikube",
                    description="",
                    runner=StepRunnerType.SHELL,
                    content="""brew install minikube"""
                )
            ]),
    ])
)

io.YamlIO.to_file('/workspaces/ggist/ggist_cli_app/resources/demo/k8s/scripts/setup.yaml', data_k8s)

