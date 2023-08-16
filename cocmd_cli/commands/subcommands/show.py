from cocmd_cli.settings import click_pass_settings
from cocmd_cli.commands.groups import show
from cocmd_cli.utils.console import console

@show.command()
@click_pass_settings
def sources(settings):
    """
    Show sources
    """
    sources = settings.sources_manager.sources

    for source in sources:
        console.print(f'{source.name}', style="white on blue")
        console.print(f' - {source.location}', style="blue")



@show.command()
@click_pass_settings
def aliases(settings):
    """
    Show aliases
    """
    
    with open(settings.aliases_file, 'r') as fin:
        line = fin.read()
        print(line)


@show.command()
@click_pass_settings
def scripts(settings):
    """
    Show scripts
    """
    available_scripts = settings.sources_manager.scripts.keys()

    
    for script in available_scripts:
        console.print(f'cocmd run {script}')
