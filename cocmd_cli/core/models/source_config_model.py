from dataclasses import dataclass
from cocmd_cli.utils.io import DictLoader
from typing import List


@dataclass(frozen=True)
class Automation:
    command: str
    file: str


@dataclass(frozen=True)
class SourceConfigModel(DictLoader):
    name: str
    aliases: str
    paths: List[str]
    automations: List[Automation]
