import argparse
import logging
import sys

from .core import main
from .log import logger

parser = argparse.ArgumentParser(sys.argv[1], description=__doc__)
parser.add_argument('repo', type=str, help='like owner/repo format')
parser.add_argument('--debug', action='store_true')
args = parser.parse_args(sys.argv[2:])

repo: str = args.repo
if args.debug:
    logger.setLevel(logging.DEBUG)

try:
    main(repo)
except KeyboardInterrupt:
    pass
