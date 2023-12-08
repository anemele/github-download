import json
import subprocess as sbp
from itertools import chain
from typing import Any, Iterable

from pick import pick

from .config import choose_repo
from .consts import COMMAND, DOWNLOAD_DIR
from .log import logger
from .mirrors import mirror_gh_ddlc_top, mirror_hub_nuaa_cf, mirror_hub_yzuu_cf
from .parser import parse_download_link, parse_gh_release_view
from .stream import get

MIRROR_SITE = (mirror_gh_ddlc_top, mirror_hub_nuaa_cf, mirror_hub_yzuu_cf)


def run(repo: str | None):
    if repo is not None:
        urls = get_download_url(repo)
    else:
        repos = choose_repo()
        urls = tuple(chain(*map(get_download_url, repos)))
    s, _ = download_release(urls)
    if s > 0:
        sbp.run(f'explorer {DOWNLOAD_DIR}')


def download_release(urls: Iterable[str]) -> tuple[int, int]:
    succ = 0
    count = 0

    for url in urls:
        count += 1
        for mirror in get_mirror_url(url):
            logger.info(f'GET {mirror}')
            resp = get(mirror)
            if resp.status_code != 200:
                continue
            path = DOWNLOAD_DIR / mirror.rsplit('/', 1)[-1]
            if path.exists():
                logger.warning(f'exists {path}')
            path.write_bytes(resp.content)
            succ += 1
            logger.info(f'SAVE {path}')

            break
        else:
            logger.warning(f'NO ACCESSIBLE RESOURCE: {url}')

    logger.info(f'FINISH {succ}/{count}')
    return succ, count


def get_mirror_url(url: str):
    for mirror in MIRROR_SITE:
        yield mirror(url)


def get_download_url(repo: str) -> Iterable[str]:
    info = get_download_info(repo)
    if info is None:
        return ()

    release, assets = info
    logger.info(f'choose {len(assets)} of {repo}')
    return (f'{release}/{asset}' for asset in assets)


def get_download_info(repo: str):
    choice = get_choices(repo)
    if choice is None:
        return

    url, assets = choice
    if assets is None or len(assets) == 0:
        logger.info(f'no choice: {repo}')
        return

    release = parse_download_link(url)
    if release is None:
        logger.info(f'no release found: {repo}')
        return

    return release, assets


def get_choices(repo: str) -> tuple[str, tuple[str, ...]] | None:
    ret = sbp.run(COMMAND.format(repo=repo), capture_output=True, encoding='ansi')
    if ret.returncode != 0:
        logger.error(f'{repo}: {ret.stderr}')
        return

    url, assets = parse_gh_release_view(ret.stdout)
    if url == '':
        logger.error(f'no release found: {repo}')
        return

    num = len(assets)
    if num == 0:
        logger.error(f'no assets found: {repo}')
        return

    logger.debug(f'{url=}')
    title = f'Please choose ASSETS (↑↓ space enter)\n{url}'
    choices = pick(assets, title, multiselect=True)
    logger.debug(f'{choices=}')

    return url, tuple(x[0] for x in choices)  # type: ignore


def query_release(repo: str) -> list[dict[str, Any]] | None:
    ret = sbp.run(f'gh api repos/{repo}/releases', capture_output=True)
    if ret.returncode != 0:
        logger.error(f'{repo}: {ret.stderr}')
        return

    return json.loads(ret.stdout)
