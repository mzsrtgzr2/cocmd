import os
from ggist_cli_app.consts import Consts
from ggist_cli_app.utils.fs import file_read_lines


class Source:

    def __init__(self, _location: str):
        self._location = _location.lower()
        if os.path.exists(self._location):
            self._aliases = tuple(file_read_lines(os.path.join(self._location, Consts.ALIASES_FILE)))
        else:
            raise

    @property
    def is_exists_locally(self):
        return False
    
    @property
    def aliases(self):
        return self._aliases
    
    def __repr__(self):
        return str(self._location)

    def __str__(self):
        return str(self._location)
