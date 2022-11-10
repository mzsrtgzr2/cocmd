import click
from ggist_cli_app.context import click_pass_context
from ggist_cli_app.core.workflow import WorkflowStep, Workflow

@click.group()
def play():
    pass

@play.command()
@click_pass_context
def flow(context):
    """
    Play a workflow
    """
    steps = [
        WorkflowStep(title='Say Hello', description='', cmd="echo 'hello'"),
        WorkflowStep(title='Download the latest release with the command', description='', cmd="""curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\""""),
        WorkflowStep(title='Validate the binary', description='', cmd="""curl -LO \"https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256\""""),
        WorkflowStep(title='Validate Sha', description='', cmd="""echo \"$(cat kubectl.sha256)  kubectl\" | sha256sum --check"""),
        WorkflowStep(title='Install in the system', description='', cmd="""sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl"""),
        WorkflowStep(title='Test', description='', cmd="""kubectl version --client"""),
        WorkflowStep(title='Cleanup', description='', cmd="""rm -rf kubectl kubectl.sha256"""),
    ]
    wf = Workflow(steps, 'osx')
    wf.play()