import click
import os
import command
from ggist_cli_app.consts import Consts 
from ggist_cli_app.context import click_pass_context


@click.command()
@click_pass_context
def apply(context):
    # apply it in bashrc with 
    # cd /workspaces/ggist/ && eval "$(python -m ggist_cli_app apply)"
    with open(context.aliases_file, 'r') as fin:
        print(fin.read())


