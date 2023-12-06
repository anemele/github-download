import argparse
import sys

from .core import main

parser = argparse.ArgumentParser(sys.argv[1], description=__doc__)
parser.add_argument('repo', type=str, help='like owner/repo format')
args = parser.parse_args(sys.argv[2:])

repo: str = args.repo
main(repo)
