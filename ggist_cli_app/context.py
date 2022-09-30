import os
import click
from ggist_cli_app.consts import Consts
from ggist_cli_app.utils.fs import mkdir

class Context:
    def __init__(self, home=None, terminal=None):
        self.home = os.path.abspath(home or Consts.HOME)
        self.terminal = terminal or Consts.DEFAULT_TERMINAL
        mkdir(self.home)


# from https://click.palletsprojects.com/en/8.1.x/complex/
click_pass_context = click.make_pass_decorator(Context, ensure=True)
