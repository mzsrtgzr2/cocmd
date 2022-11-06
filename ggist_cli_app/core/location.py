
import os
from ggist_cli_app.consts import Consts
from ggist_cli_app.utils.fs import file_read_lines


class Location:
    
    def __init__(self, _repr: str):
        self.repr = _repr

    