import sys

import click

from src.config import CLISetting, MetaInfo
from src.languages import SmartPreset, _translator
from src.misc.exceptions import EmptySentenceArgumentError
from src.misc.utils import convert_data_to_valid_string, get_type_lang, output_result, past_in_clipboard


@click.command(context_settings=CLISetting.CONTEXT_SETTINGS)
@click.version_option(version=MetaInfo.version, prog_name=MetaInfo.prog_name)
@click.argument("text", nargs=-1)
@click.option(
    "-d", "--dest",
    type=click.Choice(CLISetting.DEST_SOURCE, case_sensitive=False),
    default=CLISetting.DEFAULT_TO_DEST,
    help=CLISetting.Docs.Dest,
)
def cli(text: tuple[str], dest: str) -> None:
    r"""Translate TEXT to DEST text.

    Automatically detects the language from which you need to translate to
    another. The translation is also copied to the clipboard.

    TEXT: The sequence of characters to be translated into the language.
    DEST: One of the preset languages into which the entered sentence or
    word can be translated.

    """
    try:
        sentence = convert_data_to_valid_string(text)
    except EmptySentenceArgumentError as ex:
        click.echo(f"Error: {ex.message}", err=True)
        sys.exit(1)

    type_lang = get_type_lang(sentence)
    output_result(sentence, type_lang)
    past_in_clipboard(sentence)

    match type_lang:
        case SmartPreset.src:

            translate_text = _translator.translate(sentence, src=type_lang, dest=SmartPreset.dest).text
            style_text = click.style(f"'{3}'n'{3}'")
            click.echo()
        case SmartPreset.dest:
            click.echo("2")
        case _:
            click.echo("3")

    if type_lang == SmartPreset.src:
        print(f"'{sentence}'\n'{_translator.translate(sentence, src=type_lang, dest=SmartPreset.dest).text}'")
    elif type_lang == SmartPreset.dest:
        print(f"'{sentence}'\n'{_translator.translate(sentence, src=type_lang, dest=SmartPreset.src).text}'")
    else:
        print(f"'{sentence}'\n'{_translator.translate(sentence, src=type_lang, dest=dest).text}'")
