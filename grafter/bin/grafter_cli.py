#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generic executable.

This documentation defines how the program is run; see http://docopt.org/.

Commands:

Usage:

Options:

"""
from docopt import docopt
from grafter import generate_all
import sys


def main():
    print('try grafter cli')
    try:
        args = docopt(__doc__, version='Version number for *this* CLI')
        # some_wrapper_function(args)
        generate_all()
    except KeyboardInterrupt:
        print("Terminating CLI")
        sys.exit(1)


if __name__ == "__main__":
    main()
