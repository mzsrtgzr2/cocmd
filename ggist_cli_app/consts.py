import os
from pathlib import Path

class Consts:
    HOME=os.path.join(Path.home(), '.ggist')
    ALIASES_FILE='aliases.txt'
    DEFAULT_TERMINAL='bash'