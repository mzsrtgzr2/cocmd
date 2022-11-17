import click
from ggist_cli_app.context import click_pass_context


@click.command()
@click_pass_context
def profile_loader(context):
    # apply it in bashrc with 
    # cd /workspaces/ggist/ && eval "$(python -m ggist_cli_app apply)"

    # apply aliases
    with open(context.aliases_file, 'r') as fin:
        line = fin.read()
        print(line)


@click.command()
@click_pass_context
def refresh(context):
    context.sources_manager.save()