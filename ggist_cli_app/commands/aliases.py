import click
from ggist_cli_app.context import click_pass_context

@click.command()
@click_pass_context
def add(context):
    """
    Simple command that says hello
    """
    click.echo(f'Hello {context.home}')


