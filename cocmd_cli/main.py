import typer

from typer import Typer
from cocmd_cli.settings import Settings
from typer.models import Context


app = typer.Typer()

settings: Settings = None

@app.callback()
def main_callback(
    home: str = typer.Option(None, "--home"),
    terminal: str = typer.Option(None, "--terminal"),
):
    """
    Shared settings callback, runs before any command.
    """
    global settings
    settings = Settings(home, terminal)


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo(f"Shooting portal gun with settings: {settings.home}, {settings.terminal}")


