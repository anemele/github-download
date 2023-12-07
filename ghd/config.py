from typing import Iterable

from pick import pick

from .consts import DOWLOAD_MANIFEST
from .log import logger


def _get_manifest():
    if not DOWLOAD_MANIFEST.is_file():
        return

    return DOWLOAD_MANIFEST.read_text().strip().splitlines()


def choose_repo() -> Iterable[str]:
    manifest = _get_manifest()
    if manifest is None:
        logger.error('no repo given')
        exit(1)

    choices = pick(manifest, 'choose repos to download release', multiselect=True)
    if len(choices) == 0:
        logger.info('no choice')
        exit(0)

    choice = tuple(x[0] for x in choices)  # type: ignore
    logger.info(f'{choice=}')
    return choice
