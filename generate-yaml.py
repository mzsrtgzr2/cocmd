

from ggist_cli_app.utils import io
from ggist_cli_app.core.models.script_model import *

data = ScriptModel(
    name="setup",
    title="Setup Kubernetes",
    description="setup Kubernetes for desktop",
    spec=SpecModel(
        globals=[
            StepGlobalModel(
                    title="Instructions",
                    description="",
                    runner="readme",
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
            env="linux",
            label="debian",
            steps=[
                StepRefModel(ref="kube_instructions_md"),
                StepModel(
                    title="Install kubectl",
                    description="This will install kubectl on your machine",
                    runner="shell",
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
                    runner="shell",
                    content="""sudo apt install kubectx"""
                )
            ]),

        StepsModel(
            env="osx",
            label=">10.x.x",
            depends=[
                "installed:brew",
            ],
            steps=[
                StepModel(
                    title="Install kubectl",
                    description="This will install kubectl on your machine",
                    runner="python",
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
                    runner="shell",
                    content="""brew install kubectx"""
                ),
                StepModel(
                    title="Install kubectx",
                    description="",
                    runner="shell",
                    content="""brew install --cask lens"""
                )
            ]),
    ])
)

io.YamlIO.to_file('/workspaces/ggist/ggist_cli_app/resources/demo/k8s/scripts/setup.yaml', data)

