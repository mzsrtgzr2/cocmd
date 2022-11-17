from enum import Enum

class OS(Enum):
    ANY='any'
    OSX='osx'
    LINUX='linux'

    def __str__(self):
        return self.value

    @staticmethod
    def from_str(text: str) -> "OS":
        text = text.lower()
        for os in OS:
            if str(os).lower() == text:
                return os
        raise ValueError(f"unable to find os {text}")
