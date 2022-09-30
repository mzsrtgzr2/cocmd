import os
from pathlib import Path

class Consts:
    HOME=os.path.join(Path.home(), '.ggist')
    DEFAULT_TERMINAL='bash'