# Problem: https://adventofcode.com/2021/day/2
# Date: December 2nd, 2021
# Author: Alex Nazareth

import numpy as np

INFILE = r'day2_input'


def main():
    data = np.loadtxt(INFILE, dtype=str, delimiter='\n')

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


if __name__ == '__main__':
    print(main())
