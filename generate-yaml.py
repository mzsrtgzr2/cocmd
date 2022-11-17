

from ggist_cli_app.utils import io
from ggist_cli_app.core.models.script_model import *

data = ScriptModel(
    title="setup",
    description="setup kubectl, kubectx and kubeenvs developer environment for desktop",
    spec=[
        StepsModel(
            env="linux",
            label="debian",
            steps=[
                StepModel(
                    runner="shell",
                    content="command 1"
                )
            ]),

        StepsModel(
            env="osx",
            label=">10.x.x",
            steps=[
                StepModel(
                    runner="python",
                    content="""bla bal
bla bla
more bla 
more bla
"""
                )
            ]),
    ]
)

io.YamlIO.to_file('/workspaces/ggist/ggist_cli_app/resources/demo/k8s/scripts/setup.yaml', data)

