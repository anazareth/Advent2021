# Problem: Smoke Basin
# URL: https://adventofcode.com/2021/day/9
# Date: December 9th, 2021
# Author: Alex Nazareth

"""
Finding low points of caves given grid of floor heights.
"""

import numpy as np

INFILE = 'day9_input'


def main(data, w, l):
    x_max, y_max = w-1, l-1
    runsum = 0
    for i, row in enumerate(data):
        for j, curr_ht in enumerate(row):
            if i == 0:
                if j == 0:
                    pairs = [(i + 1, j), (i, j + 1)]
                elif j == x_max:
                    pairs = [(i + 1, j), (i, j - 1)]
                else:
                    pairs = [(i + 1, j), (i, j - 1), (i, j + 1)]
            elif j == 0:
                if i == y_max:
                    pairs = [(i - 1, j), (i, j + 1)]
                else:
                    pairs = [(i - 1, j), (i + 1, j), (i, j + 1)]
            elif i == y_max:
                if j == x_max:
                    pairs = [(i - 1, j), (i, j - 1)]
                else:
                    pairs = [(i - 1, j), (i, j - 1), (i, j + 1)]
            elif j == x_max:
                pairs = [(i - 1, j), (i + 1, j), (i, j - 1)]
            else:
                pairs = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            adj = []
            for (ii, jj) in pairs:
                adj.append(data[ii][jj])
            if all([ht > curr_ht for ht in adj]):
                runsum += curr_ht + 1
    return runsum


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str)
    data_mat = []
    for r in raw_data:
        temp = []
        for i in r:
            temp.append(int(i))
        data_mat.append(temp)
    grid_width, grid_length = len(data_mat[0]), len(data_mat)

    print(f'The sum of low point severities is {main(data_mat, grid_width, grid_length)}')
