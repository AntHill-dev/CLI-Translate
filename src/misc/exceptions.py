from abc import ABC

from colorama import Fore


class BaseErrorCLI(ABC, Exception):
    def __init__(self, message: str) -> None:
        self.message = Fore.RED + message + Fore.RESET

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return self.message


class EmptySentenceArgumentError(BaseErrorCLI):
    pass
