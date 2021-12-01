# Problem: https://adventofcode.com/2021/day/1
# Date: December 1st, 2021
# Author: Alex Nazareth

import numpy as np

INFILE = r'day1/day1_input'


def main():
    in_data = np.loadtxt(INFILE, dtype=int, delimiter='\n')

    prev = in_data[0]
    counter = 0
    for val in in_data[1:]:
        if val > prev:
            counter += 1
        prev = val
    return counter


if __name__ == '__main__':
    print("The number of increases in seafloor elevation is: %d." % main())
