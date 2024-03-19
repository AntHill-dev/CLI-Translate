from abc import ABC

from colorama import Fore  # type: ignore


class BaseErrorCLI(ABC, Exception):  # noqa: N818
    """Base class for exception to CLI-Translate.

    Each error message is painted red.
    """

    def __init__(self, message: str) -> None:
        self.message = Fore.RED + message + Fore.RESET

    def __str__(self) -> str:
        return self.message  # type: ignore

    def __repr__(self) -> str:
        return self.message  # type: ignore


class EmptySentenceArgumentError(BaseErrorCLI):
    """Exception for case empty enter data from user in CLI."""


class LanguageNotSupportedError(BaseErrorCLI):
    """Exception for case not supported dest language."""
