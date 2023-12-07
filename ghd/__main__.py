import argparse
import logging
import sys

from .config import choose_repo
from .core import run
from .log import logger


def main(repo):
    try:
        run(repo)
    except KeyboardInterrupt:
        pass


parser = argparse.ArgumentParser(sys.argv[1], description=__doc__)
parser.add_argument(
    'repo',
    type=str,
    nargs='?',
    help='like owner/repo format. default: read from manifest',
)
parser.add_argument('--debug', action='store_true')
args = parser.parse_args(sys.argv[2:])

repo: str | None = args.repo
if args.debug:
    logger.setLevel(logging.DEBUG)

if repo is None:
    for repo in choose_repo():
        main(repo)
else:
    main(repo)
