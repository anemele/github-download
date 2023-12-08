import re


def parse_download_link(url: str) -> str | None:
    # https://github.com/{owner}/{repo}/releases/tag/{v1.12.5}
    pattern = re.compile(r'https://github.com/.+?/.+?/releases/tag/\w+?')
    if pattern.match(url) is None:
        return
    # https://{host}/{owner}/{repo}/releases/download/{tag}/{file}
    # return without the tail {file}
    return url.replace('releases/tag', 'releases/download')
