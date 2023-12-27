import argparse

from github_download.config import add_manifest

from .core import run

parser = argparse.ArgumentParser(prog=__package__, description=__doc__)
parser.add_argument(
    'repo',
    type=str,
    nargs='?',
    help='like owner/repo format. default: read from manifest',
)
parser.add_argument('--add', action='store_true', help='add to manifest')
args = parser.parse_args()

repo: str | None = args.repo
if args.add:
    if repo is not None:
        add_manifest(repo)
    exit()

try:
    run(repo)
except KeyboardInterrupt:
    pass
