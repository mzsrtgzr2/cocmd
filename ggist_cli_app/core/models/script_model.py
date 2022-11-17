from dataclasses import dataclass, field
from ggist_cli_app.utils.io import DictLoader
from typing import List, Optional


@dataclass(frozen=True)
class StepModel(DictLoader):
    title: str
    description: str
    runner: str
    content: str
    
@dataclass(frozen=True)
class StepsModel(DictLoader):
    steps: List[StepModel]
    env: str
    label: str
    depends: Optional[List[str]] = field(default=None)

@dataclass(frozen=True)
class ScriptModel(DictLoader):
    title: str
    description: str
    spec: List[StepsModel]

