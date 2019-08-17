#!/usr/bin/env python

'''
roll.py:
Simulates rolls of different varieties of dice.
'''

__author__ = 'Alex Warren'

import argparse


def print_outcome(dice):
    print(dice)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dice_list', nargs='*', help='<# of dice>d<die type>')

    args = parser.parse_args()
    
    for d in args.dice_list:
        print_outcome(d)