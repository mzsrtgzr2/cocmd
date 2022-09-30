import click


@click.command()
@click.argument('name', nargs=1)
def source(name):
    """
    Simple command that says hello
    """
    


