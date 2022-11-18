import click
from ggist_cli_app.settings import click_pass_settings
from ggist_cli_app.core.sources_manager import SourcesManager
from ggist_cli_app.utils.io import file_write_lines
from ggist_cli_app.commands.groups import show

@show.command()
@click_pass_settings
def sources(settings):
    """
    Show sources
    """
    sources = SourcesManager.load_sources(settings.sources_file, context)

    print('sources:')
    for source in sources:
        print(f' - {source}')



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
    available_scripts = tuple(
        f'{source._location}.{script.name}'
        for source in settings.sources_manager.sources
        for script in source._scripts
        if source._scripts
    )
    
    for script in available_scripts:
        print(f'ggist run script {script}')
