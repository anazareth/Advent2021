# Problem: https://adventofcode.com/2021/day/1
# Date: December 1st, 2021
# Author: Alex Nazareth

import numpy as np

INFILE = r'day1/day1_input'


def part1():
    in_data = np.loadtxt(INFILE, dtype=int, delimiter='\n')

    prev = in_data[0]
    counter = 0
    for val in in_data[1:]:
        if val > prev:
            counter += 1
        prev = val
    return counter


def part2(w_size):
    in_data = np.loadtxt(INFILE, dtype=int, delimiter='\n')

    prev = sum(in_data[0:w_size])
    counter = 0
    i = w_size
    for val in in_data[w_size:]:
        rollsum = sum(in_data[i-w_size+1:i+1])
        if rollsum > prev:
            counter += 1
        prev = rollsum
        i += 1
    return counter


if __name__ == '__main__':
    print("The number of increases in seafloor elevation is: %d." % part1())
    print("When considering the sum of the last 3 data points, "
          "the number of increases in seafloor elevation is: %d." % part2(3))