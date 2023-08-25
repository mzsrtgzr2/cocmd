from cocmd_cli import resources
import os
from cocmd_cli.core.source import Source
from cocmd_cli.settings import Settings

from cocmd_cli.utils.repository import find_cocmd_files

MD_TECH = """
---
sidebar_position: {position}
---

# {name}

"""

if __name__ == "__main__":
    demo_path = os.path.join(os.path.dirname(resources.__file__), "demo")
    locations = find_cocmd_files(demo_path, 2)

    settings = Settings()

    for ii, loc in enumerate(locations):
        source = Source(loc, settings)

        with open(f"./website/docs/technologies/{source.name}", "w") as fp:
            fp.write(MD_TECH.format(name=source.name, position=ii + 1))
