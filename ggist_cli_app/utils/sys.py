import platform
from ggist_cli_app.core.os import OS

def get_os()->OS:
    return OS(platform.system().lower())