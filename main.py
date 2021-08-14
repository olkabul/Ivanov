from basic import print_line
from circumflex import print_circumflex_under
from machine_read import print_machine_read

import argparse
parser = argparse.ArgumentParser(description='Search results formatting')
group = parser.add_mutually_exclusive_group()
group.add_argument('-u', '--under', action='store_true', help='Adding "^" symbol under first character of string')
group.add_argument('-m', '--machine', action='store_true', help='Printing in machine-readable format,separated by ":"')
args = parser.parse_args()

if args.under:
    print_circumflex_under()
elif args.machine:
    print_machine_read()
else:
    print_line()