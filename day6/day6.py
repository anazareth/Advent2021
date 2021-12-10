# Problem: Lanternfish
# URL: https://adventofcode.com/2021/day/6
# Date: December 6th, 2021
# Author: Alex Nazareth

"""
Modeling lanternfish population.
- each fish spawns a new one after 7 days (+ 2 days to grow after initial spawn)
- define each fish by number of days until it spawns a new one
-
"""

import numpy as np
INFILE = r'day6_input'  # text file with input data provided by AoC2021


def part1(data, n):
    """

    :param n: int, number of days to simulate
    :param data: ndarray of int64, numbers representing time-to-spawn of each fish
    :return: int, number of lanternfish after n days
    """

    new_fish_value = 8
    just_spawned_value = 6

    # # OLD and inefficient implementation
    # for day in range(n):
    #     new_spawns = []
    #     data += -1  # decrease fish counters
    #     for i, fish in enumerate(data):
    #         if fish == -1:  # fish just spawned
    #             new_spawns.append(new_fish_value)  # add a new one
    #             data[i] = just_spawned_value  # reset counter
    #     data = np.append(data, new_spawns)

    # smart implementation: track count of fish in each group by time-to-spawn
    count_fish = dict.fromkeys(range(new_fish_value + 1), 0)
    for f in data:
        count_fish[f] += 1
    for ts in range(n):
        temp = count_fish[0]  # number of fish to spawn this step
        for i in range(new_fish_value):
            count_fish[i] = count_fish[i+1]  # move fish to next lower group
        count_fish[new_fish_value] = temp  # newly born fish
        count_fish[just_spawned_value] += temp  # fish who just spawned
    return sum(count_fish.values())


if __name__ == '__main__':
    DAYS_TO_SIMULATE = 256
    raw_data = np.loadtxt(INFILE, delimiter=',', dtype=int)
    print(f'The number of lanternfish after {DAYS_TO_SIMULATE} days is'
          f' {part1(raw_data, DAYS_TO_SIMULATE)}')
