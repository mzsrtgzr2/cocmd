import click
from ggist_cli_app.context import click_pass_context
from ggist_cli_app.core.script_runner import ScriptRunner
import inquirer
from ggist_cli_app.utils.console import console, error_console

@click.command()
@click.argument('name',  required=False)
@click_pass_context
def run(context, name: str):
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

        ScriptRunner.run(script, context.os)

    else:
        error_console.print('I don\'t know this script')        
