#!/usr/bin/env python

from __future__ import print_function

import argparse
import fileinput
import re

parser = argparse.ArgumentParser(description="Finds and prints Java Stack Traces that match the given pattern.")
parser.add_argument('pattern', help='A regex that stack traces should match to be printed.')
parser.add_argument('-b', '--begin', default='^"', help='A regex that marks the beginning of a stack trace.')
parser.add_argument('-e', '--end', default='^$', help='A regex that marks the end of a stack trace.')
parser.add_argument('-v', '--invert', action='store_true', default=False, help='Print when NOT matching the pattern.')
parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.1')
parser.add_argument('files', nargs='*', help='A list of files to be parsed, defaults to stdin.')
args = parser.parse_args()

lines = fileinput.input(args.files)
for line in lines:
    trace = line
    if re.search(args.begin, trace):
        try:
            while not re.search(args.end, line):
                line = lines.next()
                trace += line
        except StopIteration:
            pass

    if re.search(args.pattern, trace):
        if not args.invert:
            print(trace, end='')
    elif args.invert:
        print(trace, end='')
