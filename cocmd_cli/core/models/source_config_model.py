from dataclasses import dataclass
from cocmd_cli.utils.io import DictLoader


@dataclass(frozen=True)
class SourceConfigModel(DictLoader):
    name: str
