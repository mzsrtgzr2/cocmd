import click
import os
import command
from ggist_cli_app.consts import Consts 
from ggist_cli_app.context import click_pass_context


@click.command()
@click_pass_context
def apply(context):
    res = command.run(['source', context.aliases_file])
    print(res.output)


