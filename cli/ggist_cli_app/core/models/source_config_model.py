from dataclasses import dataclass, field
from cocmd_cli_app.core.os import OS
from cocmd_cli_app.utils.io import DictLoader
from typing import List, Optional, Union
from enum import Enum


@dataclass(frozen=True)
class SourceConfigModel(DictLoader):
    name: str
