#!/usr/bin/env python

'''
roll.py:
Simulates rolls of different varieties of dice.
'''

__author__ = 'Alex Warren'

import argparse
import re
import random


def validate_format(dice):
    is_valid = False

    if re.match(r'\d{1,2}d\d{1,2}', dice):
        num_dice = int( re.findall(r'^\d{1,2}', dice)[0] )

        die_type = int( re.findall(r'\d{1,2}$', dice)[0] )

        faces = (4, 6, 8, 10, 20)
        DIE_TYPES = frozenset(faces)
        
        if die_type in DIE_TYPES:
            is_valid = True
    
    return (is_valid, num_dice, die_type)


def print_outcome(num_dice, die_type):
    sum = 0
    for i in range(num_dice):
        roll = random.randint(1, die_type)
        sum += roll
        print(roll, end=' ')
    print('= %d' % sum)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('dice_list', nargs='*', help='<# of dice>d<die type>')

    args = parser.parse_args()
    
    for d in args.dice_list:
        print('%s:' % d)
        is_valid, num_dice, die_type = validate_format(d)
        if is_valid:
            print_outcome( num_dice, die_type )
        else:
            parser.print_help()
            print('\n')
            exit()
