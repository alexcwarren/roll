#!/usr/bin/env python

'''
roll.py:
Simulates rolls of different varieties of dice.
'''

__author__ = 'Alex Warren'

import argparse
import re


def valid_format(dice):
    if re.match(r'\d{1,2}d\d{1,2}', dice):
        die_type = re.findall(r'\d{1,2}$', dice)

        DIE_TYPES = [4, 6, 8, 10, 20]

        if die_type in DIE_TYPES:
            return True
    return False


def print_outcome(dice):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dice_list', nargs='*', help='<# of dice>d<die type>')

    args = parser.parse_args()
    
    for d in args.dice_list:
        if valid_format(d):
            print_outcome(d)
