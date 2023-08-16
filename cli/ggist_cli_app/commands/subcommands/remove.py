import click
from cocmd_cli_app.settings import click_pass_settings
from cocmd_cli_app.commands.groups import remove
from cocmd_cli_app.core.source import Source



@remove.command(name="source")
@click.argument('source')
@click_pass_settings
def remove_source(settings, source: str):
    """
    remove a source
    """
    source = Source(source, settings)
    settings.sources_manager.remove_source(source)
