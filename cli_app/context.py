import os


class Context:
    def __init__(self, home=None):
        self.home = os.path.abspath(home or '.')
        
    