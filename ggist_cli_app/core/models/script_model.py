from dataclasses import dataclass
from ggist_cli_app.utils.readers import DictLoader
from typing import List


@dataclass(frozen=True)
class StepModel(DictLoader):
    runner: str
    content: str
    
@dataclass(frozen=True)
class StepsModel(DictLoader):
    steps: List[StepModel]
    env: str
    label: str

@dataclass(frozen=True)
class ScriptModel(DictLoader):
    title: str
    description: str
    spec: List[StepsModel]

