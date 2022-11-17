import click

@click.group()
def add():
    pass

@click.group()
def remove():
    pass


@click.group(name='run')
def play():
    pass


@click.group()
def show():
    pass