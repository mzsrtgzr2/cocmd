from dataclasses import dataclass, field
from ggist_cli_app.core.os import OS
from ggist_cli_app.utils.io import DictLoader
from typing import List, Optional, Union
from enum import Enum


class StepRunnerType(Enum):
    SHELL="shell"
    MARKDOWN="markdown"


@dataclass(frozen=True)
class StepModel(DictLoader):
    title: str
    description: str
    runner: StepRunnerType
    content: str

@dataclass(frozen=True)    
class StepGlobalModel(StepModel):
    id: str

@dataclass(frozen=True)
class StepRefModel(DictLoader):
    ref: str

@dataclass(frozen=True)
class StepsModel(DictLoader):
    steps: List[Union[StepModel, StepRefModel]]
    env: OS
    label: str
    depends: Optional[List[str]] = field(default_factory=list)


@dataclass(frozen=True)
class SpecModel(DictLoader):
    variations: List[StepsModel]
    globals: Optional[List[StepGlobalModel]] = field(default=None)

@dataclass(frozen=True)
class ScriptModel(DictLoader):
    name: str
    title: str
    description: str
    spec: SpecModel

    def supports_os(self, os: OS)->bool:
        return any(os==variation.env for variation in  self.spec.variations)

    def get_variations_for_os(self, os: OS)->bool:
        return tuple(variation for variation in  self.spec.variations if os==variation.env)
