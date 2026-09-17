#!/usr/bin/env python3

"""
roll.py:
Simulates rolls of different varieties of dice.
"""

__author__ = "Alex C Warren"


import argparse
import random
import re
import sys


def validate_format(dice):
    num_dice = None
    die_type = None
    is_valid = False

    if re.match(r"\d{1,2}d\d{1,2}", dice):
        _num_dice = None
        find_num_dice = re.findall(r"^\d{1,2}", dice)
        if find_num_dice:
            _num_dice = int(find_num_dice[0])

        _die_type = None
        find_die_type = re.findall(r"\d{1,2}$", dice)
        if find_die_type:
            _die_type = int(find_die_type[0])

        faces = (4, 6, 8, 10, 20)
        DIE_TYPES = frozenset(faces)

        if _die_type in DIE_TYPES:
            num_dice = _num_dice
            die_type = _die_type
            is_valid = True

    return (is_valid, num_dice, die_type)


def print_outcome(num_dice, die_type):
    sum = 0
    for _ in range(num_dice):
        roll = random.randint(1, die_type)
        sum += roll
        print(roll, end=" ")
    print(f"= {sum}")


def terminate(exit_message=None):
    if exit_message is not None:
        print(f"{exit_message}\n")
    sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dice_list", nargs="*", help="<# of dice>d<die type>")

    args = parser.parse_args()

    if len(args.dice_list) < 1:
        parser.print_help()
        terminate()

    for d in args.dice_list:
        print(f"{d}:")
        is_valid, num_dice, die_type = validate_format(d)
        if is_valid:
            print_outcome(num_dice, die_type)
        else:
            parser.print_help()
            terminate()
