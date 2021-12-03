# Problem: Dive!
# URL: https://adventofcode.com/2021/day/2
# Date: December 2nd, 2021
# Author: Alex Nazareth

'''
Input text file where each row contains a command {forward, up, down} and
    a positive integer value. E.g. "forward 5" or "up 3".
Commands have different effects in part 1 and part 1, see respective functions for details.
Output is final horizontal position of submarine multpilied with final depth,
with both values initialized at 0.
'''

import numpy as np

INFILE = r'day2_input'


def part1(data):
    '''
    Commands "up" and "down" decrease and increase depth, respectively.
    Command "forward" increases horizontal position.
    :param data: list of strings
    :return: integer
    '''
    h_pos, d_pos = 0, 0  # horizontal position, depth
    for i in data:
        direction, val = i.split(' ')[0], int(i.split(' ')[1])
        if direction == 'forward':
            h_pos += val
        elif direction == 'up':
            d_pos -= val
        elif direction == 'down':
            d_pos += val
        else:
            print('unknown input %s' % direction)
    return h_pos*d_pos


def part2(data):
    '''
    Commands "up" and "down" decrease and increase aim, respectively.
    Command "forward" increases horizontal position AND increases depth by aim
        multiplied by value.
    :param data: list of strings
    :return: integer
    '''
    h_pos, d_pos, aim = 0, 0, 0  # horizontal position, depth, aim
    for i in data:
        direction, val = i.split(' ')[0], int(i.split(' ')[1])
        if direction == 'forward':
            h_pos += val
            d_pos += aim*val
        elif direction == 'up':
            aim -= val
        elif direction == 'down':
            aim += val
        else:
            print('unknown input %s' % direction)

    return h_pos*d_pos


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str, delimiter='\n')
    print(part1(raw_data))
    print(part2(raw_data))
