# Problem: The Treachery of Whales
# URL: https://adventofcode.com/2021/day/7
# Date: December 7th, 2021
# Author: Alex Nazareth

"""
Coordinating crab submarines to escape a giant whale.
- crab submarines can only move horizontally
- input horizontal position of crabs (one integer)
- line up all crabs using minimum fuel (moving 1 unit costs 1 unit of fuel)

"""

import numpy as np
INFILE = r'day7_input'  # text file with input data provided by AoC2021


def part1(data) -> int:
    med = int(np.median(data))  # median minimizes absolute deviation
    return np.sum(np.abs(data-med))


def part2(data) -> int:
    """
    - brute force approach, test every point between max and min for optimum
    - moving N units costs 1+2+3+...+N units of fuel
    :param data: ndarray of int, defining horizontal position of each crab sub
    :return: int, minimum fuel cost
    """

    result = np.sum(exp_fuel(data-min(data)))
    for align_point in range(min(data)+1, max(data)+1):
        fuel_cost = np.sum(exp_fuel(np.abs(data-align_point)))
        result = min(result, fuel_cost)
    return int(result)


def exp_fuel(dist):
    # sum of fuel steps 1+2+3+...+d
    return dist * (dist + 1) / 2


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=int, delimiter=',')

    print(f'The minimum fuel required is {part1(raw_data)}')
    print(f'The minimum fuel required for part 2 is {part2(raw_data)}')
