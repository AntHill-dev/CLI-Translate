from functools import partial
from typing import Optional

import click
from loguru import logger

from src.config import CLISetting
from src.languages import LanguageMark, SmartPreset, _translator, translate
from src.misc.exceptions import EmptySentenceArgumentError, LanguageNotSupportedError


def convert_data_to_valid_string(text: Optional[tuple[str, ...]]) -> str:
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
        text = tuple(click.prompt("Enter your text").split())

    result = " ".join(text).strip()
    logger.debug(f"Convert result: {result = }")

    if not result:
        msg = "You input a empty string."
        logger.error(f"Raise exc: EmptySentenceArgumentError with '{msg}' message.")
        raise EmptySentenceArgumentError(msg)

    return result


def detect_type_lang(sentence: str) -> LanguageMark:
    """Determines the lang from text and returns lang code as an enum element.

    Args:
        sentence: The input text from user.

    Raises:
        LanguageNotSupportedError: If the language mark you are defining is.
            not implemented programmatically in the LanguageMark enum.

    Returns:
        A language mark (code) as element of enum LanguageMark.

    """
    raw_type_language = _translator.detect(text=sentence).lang  # type: ignore

    logger.debug(f"Raw type lang: {raw_type_language}")

    try:
        type_language = LanguageMark.from_str(raw_type_language)
        logger.debug(f"Correct type lang: {type_language}")
    except NotImplementedError:
        msg = f"The language '{raw_type_language}' is not support"
        logger.error(f"Raise exc: LanguageNotSupported with '{msg}' message.")
        raise LanguageNotSupportedError(msg) from None

    return type_language


def output_result(sentence: str, lang_type: LanguageMark, dest: LanguageMark) -> str:
    """General function output translation to console.

    The function translates the sentence using `_trans` and outputs the result using
    `_output_text`. If the selected translation language is not correct, then a
    `LanguageNotSupportedError` exception will be raised.

    Args:
        sentence: Original user text to translate.
        lang_type: Detected language of input text.
        dest: Destination language.

    Raises:
        LanguageNotSupportedError: If selected `dest` language is not correct
            for `googletrans`.

    Returns:
        The translation of `sentence`.

    """
    logger.info(f"{lang_type = }")
    _trans = partial(translate, text=sentence, source_lang=lang_type)

    try:
        if lang_type == SmartPreset.src and SmartPreset.dest == dest:  # type: ignore
            logger.debug(f"Preset: from source ({SmartPreset.src}) to dest ({SmartPreset.dest}) [default 1]")
            translate_text = _trans(dest_lang=SmartPreset.dest)  # type: ignore
            _output_text(sentence, translate_text)
        elif lang_type == SmartPreset.dest and SmartPreset.dest == dest:  # type: ignore
            logger.debug(f"Preset: from dest ({SmartPreset.dest}) to source ({SmartPreset.src}) [default 2]")
            translate_text = _trans(dest_lang=SmartPreset.src)  # type: ignore
            _output_text(sentence, translate_text)
        else:
            logger.debug(f"Preset: from dest ({SmartPreset.dest}) to source ({SmartPreset.src})")
            translate_text = _trans(dest_lang=dest)
            _output_text(sentence, translate_text)
    except ValueError:
        msg = f"During translate the language '{lang_type}' is not support"
        logger.error(f"Raise exc: LanguageNotSupported with '{msg}' message.")
        raise LanguageNotSupportedError(msg) from None

    logger.info(f"Translated text: {translate_text}")
    return translate_text


def _output_text(original: str, translated: str) -> None:
    """Shortcut function for stylized output."""
    click.echo("Original: " + click.style(f"{original}", fg=CLISetting.Colors.Original))
    click.echo("Translated: " + click.style(f"{translated}", fg=CLISetting.Colors.Translated))
