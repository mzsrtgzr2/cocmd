from dacite import from_dict
from dataclasses import asdict, dataclass
import yaml
from typing import Dict


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
            obj = cls(obj)
        return obj

    @staticmethod
    def to_file(file: str, data: DictLoader):
        with open(file, "w") as fp:
            yaml.dump(data.to_dict(), fp, default_flow_style=False)

