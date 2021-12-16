# Problem: Syntax Scoring
# URL: https://adventofcode.com/2021/day/10
# Date: December 10th, 2021
# Author: Alex Nazareth

"""

"""

import numpy as np

INFILE = 'day10_input'


def part1(data) -> int:
    point_values = {')': 3, ']': 57, '}': 1197, '>': 25137}
    open_brackets = {'(', '[', '{', '<'}
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    data_uncorrupted = []
    syntax_score = 0
    for row in data:
        row_is_uncorrupted = True
        stack = []
        for c in row:
            if c in open_brackets:
                stack.append(c)
            else:
                if brackets[stack[-1]] == c:
                    stack.pop()
                else:
                    syntax_score += point_values[c]
                    row_is_uncorrupted = False
                    break
        if row_is_uncorrupted:
            data_uncorrupted.append(row)
    return syntax_score, data_uncorrupted


def part2(data):
    point_values = {')': 1, ']': 2, '}': 3, '>': 4}
    brackets = {'(': ')', '[': ']', '{': '}', '<': '>'}
    open_brackets = {'(', '[', '{', '<'}

    autocomplete_scores = []
    for row in data:
        stack = []
        for c in row:
            if c in open_brackets:
                stack.append(c)
            else:
                stack.pop()
        if len(stack) != 0:
            row_score = 0
            for _ in range(len(stack)):
                row_score = 5*row_score + point_values[brackets[stack.pop()]]
            autocomplete_scores.append(row_score)
    return np.median(sorted(autocomplete_scores))



if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, delimiter='\n', dtype=str)

    s_score, uncorrupted = part1(raw_data)
    print(f'The syntax error score is {s_score}')
    print(f'The middle autocomplete score is {part2(uncorrupted)}')
