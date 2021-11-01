import sys
import argparse
from qgraph import qgraph_lib


def run_cli():
    # command line parsing
    parser = argparse.ArgumentParser(description='Quickly display a chart for data read from stdin')
    parser.add_argument('--title', help='Graph title')
    subparsers = parser.add_subparsers(dest='subparser_name', help='sub-command help')
    line = subparsers.add_parser('line', help='draw line graph')
    bar = subparsers.add_parser('bar', help='draw bar graph')
    pie = subparsers.add_parser('pie', help='draw pie graph')
    histogram = subparsers.add_parser('histogram', help='draw histogram')
    args = parser.parse_args()
    if args.subparser_name == None:
        args.subparser_name = 'line'

    # process input
    nums = qgraph_lib.txt_to_nums(sys.stdin.readlines())
    # nums = (1, 2, 4, 3, 8)

    # draw graph
    qgraph_lib.graph(nums, title=args.title, style=args.subparser_name)


if __name__ == '__main__':
    run_cli()
