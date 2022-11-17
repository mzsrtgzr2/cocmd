import click
from ggist_cli_app.commands.groups import play
from ggist_cli_app.context import click_pass_context
from ggist_cli_app.core.script_runner import ScriptRunner
import inquirer
from ggist_cli_app.utils.console import console, error_console

# scriptS = {
#     'k8s-setup': Workscript([
#         WorkscriptStep(title='Download the latest release with the command', description='', cmd={
#             OS.linux: WorkscriptCommand("""curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\""""),
#             OS.osx: WorkscriptCommand("""curl -LO \"https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl\""""),
#         }),
#         WorkscriptStep(title='Validate the binary', description='', cmd={
#             OS.linux: WorkscriptCommand("""curl -LO \"https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256\""""),
#             OS.osx: WorkscriptCommand("""curl -LO \"https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256\""""),
#         }),
#         WorkscriptStep(title='Validate Sha', description='', cmd={
#             OS.linux: WorkscriptCommand("""echo \"$(cat kubectl.sha256)  kubectl\" | sha256sum --check"""),
#             OS.osx: WorkscriptCommand("""echo \"$(cat kubectl.sha256)  kubectl\" | sha256sum --check"""),
#         }),
#         WorkscriptStep(title='Install in the system', description='', cmd={
#             OS.linux: WorkscriptCommand("""sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl"""),
#             OS.osx: WorkscriptCommand("""sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl"""),
#         }),
#         WorkscriptStep(title='Test', description='', cmd={
#             OS.any: WorkscriptCommand("""kubectl version --client"""),
#         }),
#         WorkscriptStep(title='Cleanup', description='', cmd={
#             OS.linux: WorkscriptCommand("""rm -rf kubectl kubectl.sha256"""),
#             OS.osx: WorkscriptCommand("""rm -rf kubectl kubectl.sha256"""),
#         }),
#     ], None),
#     'awscli-setup': Workscript([ # https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
#         WorkscriptStep(title='Download the pkg installer', description='', cmd={
#             OS.osx: WorkscriptCommand("""curl \"https://awscli.amazonaws.com/AWSCLIV2.pkg\" -o \"AWSCLIV2.pkg\""""),
#             OS.linux: WorkscriptCommand("""curl \"https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip\" -o \"awscliv2.zip\""""),
#         }),
#         WorkscriptStep(title='Run the pkg installer', description='', cmd={
#             OS.osx: WorkscriptCommand("""sudo installer -pkg AWSCLIV2.pkg -target /"""),
#             OS.linux: WorkscriptCommand("""unzip awscliv2.zip && sudo ./aws/install"""),
#         }),
#         WorkscriptStep(title='Validation', description='', cmd={
#             OS.osx: WorkscriptCommand("""aws --version"""),
#             OS.linux: WorkscriptCommand("""aws --version"""),
#         }),
#         WorkscriptStep(title='Configure', description='', cmd={
#             OS.osx: WorkscriptCommand("""aws configure"""),
#             OS.linux: WorkscriptCommand("""aws configure"""),
#         }),
#     ], None),

# }
@play.command()
@click.argument('name',  required=False)
@click_pass_context
def script(context, name: str):
    """
    Run something
    """

    available_scripts = {
        f'{source._location}.{script.name}': script
        for source in context.sources_manager.sources
        for script in source._scripts
        if source._scripts
    }

    if not name:
        questions = [
            inquirer.List(
                "script",
                message="What script to run?",
                choices=tuple(available_scripts.keys()),
            ),
        ]

        answers = inquirer.prompt(questions)
        name = answers['script']


    if name in available_scripts:
        script = available_scripts[name]    

        if not script.supports_os(context.os):
            error_console.print('This script not supporting your os') 
            return

        ScriptRunner.run(script)

    else:
        error_console.print('I don\'t know this script')        
