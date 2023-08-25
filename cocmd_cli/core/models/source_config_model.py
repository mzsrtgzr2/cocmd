from dataclasses import dataclass
from cocmd_cli.utils.io import DictLoader, YamlIO, normalize_path
from typing import List, Optional
from .script_model import ScriptModel


@dataclass(frozen=True)
class Automation:
    subcommand: str
    file: Optional[str]
    content: Optional[ScriptModel]

    def load_content(self, location: str):
        if self.file:
            self.content = YamlIO.from_file(
                normalize_path(self.file, location),
                cls=ScriptModel,
            )


@dataclass(frozen=True)
class SourceConfigModel(DictLoader):
    name: str
    aliases: str
    paths: List[str]
    automations: List[Automation]
