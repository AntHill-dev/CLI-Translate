import sys
from typing import NoReturn

import click
import pyperclip  # type: ignore
from loguru import logger

from src.config import CLISetting, MetaInfo
from src.languages import LanguageMark, SmartPreset
from src.misc.exceptions import EmptySentenceArgumentError, LanguageNotSupportedError
from src.misc.utils import convert_data_to_valid_string, detect_type_lang, output_result


def _report_about_error(msg: str) -> NoReturn:
    click.echo(f"Error: {msg}", err=True)
    sys.exit(1)


@click.command(context_settings=CLISetting.CONTEXT_SETTINGS)
@click.version_option(version=MetaInfo.version, prog_name=MetaInfo.prog_name)
@click.argument("text", nargs=-1)
@click.option(
    "-d",
    "--dest",
    type=click.Choice(LanguageMark, case_sensitive=False),  # type: ignore
    default=SmartPreset.dest,
    help=CLISetting.Docs.Dest,
)
def cli(text: tuple[str], dest: LanguageMark) -> None:
    r"""Translate TEXT to DEST text.

    Automatically detects the language from which you need to translate to
    another. The translation is also copied to the clipboard.

    TEXT: The sequence of characters to be translated into the language.
    DEST: One of the preset languages into which the entered sentence or
    word can be translated.

    """
    logger.info(f"INPUT {text = }, type: {type(text)}")
    logger.info(f"INPUT {dest = }, type: {type(dest)}")

    try:
        sentence = convert_data_to_valid_string(text)
    except EmptySentenceArgumentError as ex:
        _report_about_error(ex.message)

    try:
        type_lang = detect_type_lang(sentence)
        to_copy_sentence = output_result(sentence, type_lang, dest)
    except LanguageNotSupportedError as ex:
        _report_about_error(ex.message)

    # copy to clipboard
    pyperclip.copy(to_copy_sentence)
