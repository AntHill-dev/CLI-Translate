from typing import Optional

import click
from loguru import logger

from src.languages import _translator
from src.misc.exceptions import EmptySentenceArgumentError


def convert_data_to_valid_string(text: Optional[tuple[str]]) -> str:
    """Converts a tuple of strings to a single string.

    If the function accepts None, then it requests input from the user.

    Args:
        text: Input data from user or None.

    Raises:
        EmptySentenceArgumentError: If you entered an empty line.


    Returns:
        A single string.

    """
    if not text:
        text = tuple(click.prompt("Enter you text").split())

    result = " ".join(text).strip()
    logger.debug(f"Convert result: {result = }")

    if not result:
        msg = "You input a empty string."
        logger.error("Raise exc: EmptySentenceArgumentError with 'You input a empty string.' message.")
        raise EmptySentenceArgumentError(msg)

    return result


def get_type_lang(sentence: str) -> str:
    type_language = _translator.detect(text=sentence).lang
    return type_language


def output_result(sentence: str, lang_type: str) -> None:
    pass


def past_in_clipboard(sentence: str) -> None:
    pass
