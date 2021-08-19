from basic import get_results_basic_list
from circumflex import get_results_with_circumflex
from machine_read import get_results_by_machine_read

def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser(description='Search results formatting')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-u', '--under', action='store_true', help='Adding "^" symbol under first character of string')
    group.add_argument('-m', '--machine', action='store_true', help='Printing in machine-readable format,separated by ":"')
    args = parser.parse_args()
    return args

def get_result_by_argument(args):
    if args.under:
        result = get_results_with_circumflex()
    elif args.machine:
        result = get_results_by_machine_read()
    else:
        result = get_results_basic_list()
    return result

def main():
    args = parse_arguments()
    result = get_result_by_argument(args)
    print(result)

if __name__ == '__main__':
  main()