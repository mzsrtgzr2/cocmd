


import itertools
from typing import Sequence
from ggist_cli_app.core.source import Source
from ggist_cli_app.utils.fs import file_write_lines


def recreate_aliases(dest_aliases:str, sources: Sequence[Source]):

    def _assert_alias_line(s):
        if not s:
            return s
        if not s.startswith('alias '):
            return f'alias {s}'
        return s

    file_write_lines(dest_aliases, itertools.chain.from_iterable(
        map(_assert_alias_line, source.aliases)
        for source in sources
    ))