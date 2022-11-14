import click
from ..groups import add
from ggist_cli_app.context import click_pass_context
from ggist_cli_app.core.source import Source
from ggist_cli_app.utils.fs import file_write_lines


@add.command()
@click.argument('source')
@click_pass_context
def source(context, source: str):
    """
    add a source
    """
    source = Source(source, context)
    context.sources.add_source(source)
    context.sources.remove_source(source)