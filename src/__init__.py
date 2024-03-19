import click
import colorama  # type: ignore
from loguru import logger

import src.misc.logs as lg
from src import config
from src.main import cli
from src.misc.exceptions import BaseErrorCLI

__author__ = config.MetaInfo.author
__copyright__ = config.MetaInfo.copyright
__license__ = config.MetaInfo.license
__version__ = config.MetaInfo.version

__maintainer__ = config.MetaInfo.maintainer
__email__ = config.MetaInfo.email
__status__ = config.MetaInfo.status

colorama.init()
lg.init(__debug__)


@logger.catch()
def start_cli() -> None:  # noqa: D103
    try:
        cli()
    except BaseErrorCLI as ex:
        logger.error(f"error: {ex}")
        click.echo(f"Error: {ex.message}")
