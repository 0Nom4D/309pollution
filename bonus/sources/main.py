#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 309pollution
## File description:
## main
##

from sources.ArgChecker import ArgChecker
from sources.Pollution import Pollution
from sources.exitCode import exitCode
from sys import argv


def print_usage() -> int:
    print("USAGE\n\t./309pollution n file x y\n"
          "DESCRIPTION\n"
          "\tn\tnumber of points on the grid axis\n"
          "\tfile\tcsv file containing the data points x;y;p\n"
          "\tx\tabscissa of the point whose pollution level we want to know\n"
          "\ty\tordinate of the point whose pollution level we want to know"
          )
    return exitCode.OK


def main() -> int:
    arg_checker = ArgChecker()
    if len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help'):
        return print_usage()
    elif len(argv) != 5:
        return exitCode.ERROR
    if not arg_checker.check_args_conformity(argv[1:]):
        return exitCode.ERROR
    pollution_engine = Pollution(arg_checker.numericalArgs, arg_checker.fileContent)
    pollution_engine.launch_engine()
    return exitCode.OK


if __name__ == '__main__':
    exit(main())
