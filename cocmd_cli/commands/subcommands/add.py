import click
from ..groups import add
from cocmd_cli.settings import click_pass_settings
from cocmd_cli.core.source import Source
from cocmd_cli.utils.io import file_write_lines
import inquirer
from cocmd_cli.utils.console import console, error_console


@add.command()
@click.argument('source')
@click_pass_settings
def source(settings, source: str):
    """
    add a source
    """

    source_label = source
    source = Source(source_label, settings)
    console.print(f'''This will add:
    - {len(source.aliases)} aliases
    - {len(source.scripts)} scripts
    ''')
    questions = [
        inquirer.Confirm("sure", message="Continue?", default=True),
    ]

    answers = inquirer.prompt(questions)

    if answers['sure']:        
        settings.sources_manager.add_source(source)
        console.print(f"[bold green]Source '{source}' added")
        if source.aliases:
            console.print(f"open a new terminal session and you can use:")
            for alias in source.aliases[:10]:
                console.print(f'-{alias}')

            if len(source.aliases) > 10:
                console.print('...\n(partial)')
            console.print('[blue] to see the full list run `cocmd show aliases`')
    else:
        console.print("[bold red]Skipped. you answered 'NO'")