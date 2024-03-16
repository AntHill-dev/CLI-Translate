import click

from src.config import CLISetting
from src.misc.utils import get_only_letters_from


@click.command(context_settings=CLISetting.CONTEXT_SETTINGS)
@click.option("--sentence", prompt="Enter your sentence", help="Initial sentence to be translated.")
@click.option("--to-lang", type=click.Choice(["MD5", "SHA1"], case_sensitive=False))
def cli(sentence: str, to_lang: str) -> None:
    letters = get_only_letters_from(sentence)
    click.echo(letters)

    click.echo(sentence)
    click.echo(to_lang)
