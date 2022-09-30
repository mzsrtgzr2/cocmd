from pathlib import Path

def mkdir(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)

def touch(file):
    Path(file).touch()