import os
from pathlib import Path
import click
from ggist_cli_app.consts import Consts


class Context:
    def __init__(self, home=None):
        self.home = os.path.abspath(home or Consts.HOME)
        
        self._init_root_folder()

    def _init_root_folder(self):
        Path(self.home).mkdir(parents=True, exist_ok=True)

# from https://click.palletsprojects.com/en/8.1.x/complex/
click_pass_context = click.make_pass_decorator(Context, ensure=True)
