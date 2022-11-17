from dataclasses import dataclass, field
from ggist_cli_app.utils.io import DictLoader
from typing import List, Optional, Union


@dataclass(frozen=True)
class StepModel(DictLoader):
    title: str
    description: str
    runner: str
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
    env: str
    label: str
    depends: Optional[List[str]] = field(default_factory=list)


@dataclass(frozen=True)
class SpecModel(DictLoader):
    variations: List[StepsModel]
    globals: Optional[List[StepGlobalModel]] = field(default=None)

@dataclass(frozen=True)
class ScriptModel(DictLoader):
    title: str
    description: str
    spec: SpecModel


