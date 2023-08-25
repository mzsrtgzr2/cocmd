from typing import List
import click

from cocmd_cli.consts import Consts
from cocmd_cli.core.source import Source
from ..groups import add
from cocmd_cli.settings import click_pass_settings
import inquirer
from cocmd_cli.utils.console import console
from cocmd_cli import resources
import os


@add.command()
@click.argument("source")
@click_pass_settings
def source(settings, source: str):
    """
    add a source
    """

    source_label = source

    if source_label == "demo":
        source_label = os.path.join(os.path.dirname(resources.__file__), source_label)

    locations = _find_cocmd_files(source_label, settings.scan_depth)

    lst_locs = "\n  - ".join(locations)
    console.print(
        f"""found {len(locations)} cocmd sources in this path:
  - {lst_locs}
    """
    )
    questions = [
        inquirer.Confirm("sure", message="Continue?", default=True),
    ]

    answers = inquirer.prompt(questions)

    if answers["sure"]:
        for loc in locations:
            source = Source(loc, settings)
            settings.sources_manager.add_source(source)
            console.print(f"[bold green]Source '{source}' added")
    else:
        console.print("[bold red]Skipped. you answered 'NO'")


def _find_cocmd_files(source_label: str, scan_depth: int) -> List[str]:
    locations = []
    depth = 0

    for root, dirs, files in os.walk(source_label):
        if Consts.SOURCE_CONFIG_FILE in files:
            locations.append(root)
        # Counting the depth from the source_label
        relative_root = os.path.relpath(root, source_label)
        depth = relative_root.count(os.sep) if relative_root != "." else 0

        # Stop if the scan depth is reached
        if depth >= scan_depth:
            # Removing dirs will prevent os.walk from traversing deeper
            del dirs[:]

    return locations
