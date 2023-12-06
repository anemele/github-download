import subprocess as sbp

from pick import pick

from .consts import COMMAND, DOWNLOAD_DIR
from .log import logger
from .mirrors import mirror_gh_ddlc_top, mirror_hub_nuaa_cf, mirror_hub_yzuu_cf
from .parser import parse_download_link, parse_gh_release_view
from .stream import get

MIRROR_SITE = (mirror_gh_ddlc_top, mirror_hub_nuaa_cf, mirror_hub_yzuu_cf)


def main(repo: str):
    succ = 0
    count = 0
    for url in get_download_url(repo):
        count += 1
        for mirror in get_mirror_url(url):
            logger.info(f'GET {mirror}')
            resp = get(mirror)
            if resp.status_code == 200:
                path = DOWNLOAD_DIR / mirror.rsplit('/', 1)[-1]
                path.write_bytes(resp.content)
                succ += 1
                logger.info(f'SAVE {path}')

                break
        else:
            logger.warning(f'NO ACCESSIBLE RESOURCE: {url}')

    logger.info(f'FINISH {succ}/{count}')
    sbp.run(f'explorer {DOWNLOAD_DIR}')


def get_mirror_url(url: str):
    for mirror in MIRROR_SITE:
        yield mirror(url)


def get_download_url(repo: str):
    url, assets = get_choices(repo)
    if assets is None or len(assets) == 0:
        logger.info('no choice')
        exit(1)

    release = parse_download_link(url)
    if release is None:
        logger.info('no tag url found')
        exit(1)

    for asset in assets:
        yield f'{release}/{asset}'


def get_choices(repo: str) -> tuple[str, tuple[str, ...]]:
    ret = sbp.run(COMMAND.format(repo=repo), capture_output=True, encoding='ansi')
    if ret.returncode != 0:
        logger.error(ret.stderr)
        exit(1)

    url, assets = parse_gh_release_view(ret.stdout)
    if url == '':
        logger.error('no tag url found')
        exit(1)
    num = len(assets)
    if num == 0:
        logger.error('no assets found')
        exit(1)

    title = f'Please choose ASSETS (↑↓ space enter)\n{url}'
    choices = pick(assets, title, multiselect=True)
    logger.debug(f'{choices=}')

    return url, tuple(x[0] for x in choices)  # type: ignore
