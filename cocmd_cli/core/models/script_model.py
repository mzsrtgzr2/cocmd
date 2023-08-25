from dataclasses import dataclass, field
from cocmd_cli.core.os import OS
from cocmd_cli.utils.io import DictLoader
from typing import List, Optional
from enum import Enum


class StepRunnerType(Enum):
    SHELL = "shell"
    MARKDOWN = "markdown"
    PYTHON = "python"
    COCMD_SCRIPT = "cocmd_script"
    LINK = "link"


@dataclass(frozen=True)
class StepModel(DictLoader):
    title: str
    runner: StepRunnerType
    content: str
    description: str


@dataclass(frozen=True)
class ScriptModel(DictLoader):
    steps: List[StepModel]
    env: Optional[OS] = field(default=OS.ANY)
    description: Optional[str] = field(default=None)

    def supports_os(self, os: OS) -> bool:
        return os in (self.env, OS.ANY)
