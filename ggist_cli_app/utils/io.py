from dacite import from_dict
from dataclasses import asdict, dataclass
import yaml
from typing import Dict
import os
from pathlib import Path
from typing import Sequence

def exists(path)->bool:
    return os.path.exists(path)

def mkdir(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)

def touch(file):
    Path(file).touch()

def file_read_lines(file) -> Sequence[str]:
    with open(file, 'r') as fp:
        return map(lambda s: s.strip(), fp.readlines())

def file_write_lines(file, lines):
    with open(file, 'w') as fp:
        fp.writelines(map(lambda s: f'{s}\n', lines))

@dataclass(frozen=True)
class DictLoader:
    @classmethod
    def from_dict(cls, data):
        return from_dict(data_class=cls, data=data)

    def to_dict(self):
        return asdict(self)

class YamlIO:
    @staticmethod
    def from_file(file: str, cls: DictLoader=None)->DictLoader:
        with open(file, "r") as fp:
            text = fp.read()
            obj = yaml.safe_load(text)
        
        if cls:
            obj = cls.from_dict(obj)
        return obj

    @staticmethod
    def to_file(file: str, data: DictLoader):
        with open(file, "w") as fp:
            yaml.dump(data.to_dict(), fp, default_flow_style=False)

