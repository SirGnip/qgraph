import sys
import argparse
from qgraph import qgraph


def run_cli():
    parser = argparse.ArgumentParser(description='Quickly display a chart for data read from stdin')
    parser.add_argument('--title', help='Graph title')
    args = parser.parse_args()

    nums = qgraph.txt_to_nums(sys.stdin.readlines())
    qgraph.graph(nums, title=args.title)


if __name__ == '__main__':
    run_cli()
