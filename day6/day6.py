# Problem: Lanternfish
# URL: https://adventofcode.com/2021/day/6
# Date: December 6th, 2021
# Author: Alex Nazareth

"""
Modeling lanternfish population.
"""

import numpy as np
INFILE = r'day5_input'  # text file with input data provided by AoC2021


def part1(data):
    return data[0]


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, delimiter='\n')

    print(f'The solution to part 1 is {part1(raw_data)}')
