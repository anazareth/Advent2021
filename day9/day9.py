# Problem: Smoke Basin
# URL: https://adventofcode.com/2021/day/9
# Date: December 9th, 2021
# Author: Alex Nazareth

"""
Finding low points of caves given grid of floor heights.
"""

import numpy as np

INFILE = 'day9_input'


def part1(data, w, l):
    x_max, y_max = w-1, l-1
    runsum = 0
    low_points = []
    for i, row in enumerate(data):
        for j, curr_ht in enumerate(row):
            pairs = get_adj_pairs(data, i, j, x_max, y_max)
            adj = []
            for (ii, jj) in pairs:
                adj.append(data[ii][jj])
            if all([ht > curr_ht for ht in adj]):
                low_points.append((i, j))
                runsum += curr_ht + 1
    return runsum, low_points


def part2(data, w, l, l_pts):
    x_max, y_max = w - 1, l - 1
    top3 = (0, 0, 0)  # size of top 3 largest basins
    for (lp_i, lp_j) in l_pts:
        basin_size = 1 + get_basin_size(data, lp_i, lp_j, x_max, y_max, visited={(lp_i, lp_j)})
        top3 = sorted(list(top3) + [basin_size])[-3:]
    return np.product(top3)


def get_basin_size(grid, i, j, x_max, y_max, visited: set) -> int:
    pairs = get_adj_pairs(grid, i, j, x_max, y_max)
    incr_pairs = [(ii, jj) for (ii, jj) in pairs if grid[ii][jj] > grid[i][j] and grid[ii][jj] != 9]
    basin_run_sum = 0
    if len(incr_pairs) == 0:
        return 0
    else:
        for (i_adj, j_adj) in incr_pairs:
            if (i_adj, j_adj) not in visited:
                visited.add((i_adj, j_adj))
                basin_run_sum += 1 + get_basin_size(grid, i_adj, j_adj, x_max, y_max, visited)
        return basin_run_sum


def get_adj_pairs(grid, i, j, x_max, y_max) -> list:
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
    return pairs


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str)
    data_mat = []
    for r in raw_data:
        temp = []
        for c in r:
            temp.append(int(c))
        data_mat.append(temp)
    grid_width, grid_length = len(data_mat[0]), len(data_mat)

    lowpt_sum, low_points = part1(data_mat, grid_width, grid_length)
    print(f'The sum of low point severities is {lowpt_sum}')
    print(f'The product of 3 largest basins is {part2(data_mat, grid_width, grid_length, low_points)}')
