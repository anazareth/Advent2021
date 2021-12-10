# Problem: Hydrothermal Venture
# URL: https://adventofcode.com/2021/day/5
# Date: December 5th, 2021
# Author: Alex Nazareth

"""
Tracking overlap points of hydrothermal vents on a grid.
"""

import numpy as np
INFILE = r'day5_input'  # text file with input data provided by AoC2021


def part1(data) -> int:
    """
    Track vertical and horizontal paths, and count how many grid points overlap.
    :param data: set of tuples of form ((x1, y1), (x2, y2)), the start and end of a path
    :return: int, the count of points where multiple paths overlap
    """
    # dict with coordinate (x,y) as key, count of paths crossing that point as value
    visited = dict()
    overlap_points = set()
    for path in data:
        x1, y1, x2, y2 = [val for pair in path for val in pair]
        # loop through points on path, and check if each point is already in dict
        if x1 == x2:
            for y_i in range(min(y1, y2), max(y1, y2) + 1):
                if (x1, y_i) in visited:
                    visited[(x1, y_i)] += 1
                    overlap_points.add((x1, y_i))
                else:
                    visited[(x1, y_i)] = 1
        else:
            for x_i in range(min(x1, x2), max(x1, x2) + 1):
                if (x_i, y1) in visited:
                    visited[(x_i, y1)] += 1
                    overlap_points.add((x_i, y1))
                else:
                    visited[(x_i, y1)] = 1
    return len(overlap_points)


def part2(data) -> int:
    """
    Track vertical, horizontal, and diagonal (45deg only) paths,
    and count how many grid points overlap.
    :param data: set of tuples of form ((x1, y1), (x2, y2)), the start and end of a path
    :return: int, the count of points where multiple paths overlap
    """
    # dict with coordinate (x,y) as key, count of paths crossing that point as value
    visited = dict()
    overlap_points = set()
    for path in data:
        x1, y1, x2, y2 = [val for pair in path for val in pair]
        # loop through points on path, and check if each point is already in dict
        x_min, x_max = min(x1, x2), max(x1, x2)
        y_min, y_max = min(y1, y2), max(y1, y2)
        if x1 == x2:
            for y_i in range(y_min, y_max + 1):
                if (x1, y_i) in visited:
                    visited[(x1, y_i)] += 1
                    overlap_points.add((x1, y_i))
                else:
                    visited[(x1, y_i)] = 1
        elif y1 == y2:
            for x_i in range(x_min, x_max + 1):
                if (x_i, y1) in visited:
                    visited[(x_i, y1)] += 1
                    overlap_points.add((x_i, y1))
                else:
                    visited[(x_i, y1)] = 1
        else:
            x_range = range(x1, x2 + 1) if x2 > x1 else reversed(range(x2, x1 + 1))
            y_range = range(y1, y2 + 1) if y2 > y1 else reversed(range(y2, y1 + 1))

            for x_i, y_i in zip(x_range, y_range):
                if (x_i, y_i) in visited:
                    visited[(x_i, y_i)] += 1
                    overlap_points.add((x_i, y_i))
                else:
                    visited[(x_i, y_i)] = 1
    return len(overlap_points)


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, delimiter='\n', dtype=str)
    all_paths = set()
    for row in raw_data:
        x1, y1, x2, y2 = [int(val) for pair in row.split(' -> ') for val in pair.split(',')]
        all_paths.add(((x1, y1), (x2, y2)))
    horiz_vert_paths = [((x1, y1), (x2, y2)) for ((x1, y1), (x2, y2)) in
                        all_paths if x1 == x2 or y1 == y2]
    print(f'Solution to part 1: {part1(horiz_vert_paths)}')
    print(f'Solution to part 1: {part2(all_paths)}')
