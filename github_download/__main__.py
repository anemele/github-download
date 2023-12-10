import argparse
import logging
import sys

from .core import run
from .log import logger

parser = argparse.ArgumentParser(
    prog=__package__ if len(sys.argv) == 1 else sys.argv[1], description=__doc__
)
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

try:
    run(repo)
except KeyboardInterrupt:
    pass
