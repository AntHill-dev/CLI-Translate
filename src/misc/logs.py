from pathlib import Path

from loguru import logger

from src.config import RotationSettings


def init(log: bool) -> None:
    """Initializing logging.

    Enables logging and creates a folder for rotation files or disables logging.

    Args:
        log: Enables logging by this flag

    Returns:
        None
    """
    if log is False:
        path_to_log = Path(__file__).parent.parent.with_name(RotationSettings.folder) / "debug.log"
        Path.mkdir(path_to_log.parent, exist_ok=True)

        logger.add(path_to_log, rotation=RotationSettings.size, compression=RotationSettings.type)
    else:
        logger.remove()
