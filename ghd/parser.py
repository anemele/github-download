import re


def parse_download_link(url: str) -> str | None:
    # https://github.com/{owner}/{repo}/releases/tag/{v1.12.5}
    pattern = re.compile(r'https://github.com/\w+?/\w+?/releases/tag/\w+?')
    if pattern.match(url) is None:
        return
    # https://{host}/{owner}/{repo}/releases/download/{tag}/{file}
    # return without the tail {file}
    return url.replace('tag', 'download')


def parse_gh_release_view(output: str) -> tuple[str, tuple[str, ...]]:
    url = ''
    assets = []
    for line in output.splitlines():
        if line.startswith('url:'):
            _, url = line.split(maxsplit=1)
        elif line.startswith('asset:'):
            _, tmp = line.split(maxsplit=1)
            assets.append(tmp)
    return url, tuple(assets)
