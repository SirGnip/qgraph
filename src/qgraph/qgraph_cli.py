import sys
import argparse
from qgraph import qgraph_lib


def run_cli():
    # command line parsing
    parser = argparse.ArgumentParser(description='Quickly display a chart for data read from stdin')
    parser.add_argument('--title', help='Graph title')
    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')
    line = subparsers.add_parser('line', help='draw line graph')
    histogram = subparsers.add_parser('histogram', help='draw histogram')
    args = parser.parse_args()

    # process input
    # nums = qgraph_lib.txt_to_nums(sys.stdin.readlines())
    nums = (1, 2, 4, 3, 8)

    # draw graph
    print('sub prog:', args.subparser_name)
    qgraph_lib.graph(nums, title=args.title, type=args.subparser_name)


if __name__ == '__main__':
    run_cli()
