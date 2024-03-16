import click
import colorama
from loguru import logger

import src.misc.logs as lg
from src import config
from src.main import cli
from src.misc import exceptions

__author__ = config.MetaInfo.author
__copyright__ = config.MetaInfo.copyright
__license__ = config.MetaInfo.license
__version__ = config.MetaInfo.version

__maintainer__ = config.MetaInfo.maintainer
__email__ = config.MetaInfo.email
__status__ = config.MetaInfo.status

colorama.init()
lg.init(__debug__)


def main() -> None:
    try:
        cli()
    except exceptions.EmptySentenceArgumentError as exc:
        logger.error(f"error: {exc}, {exc.message}")
        click.echo(f"Error: {exc.message}")
