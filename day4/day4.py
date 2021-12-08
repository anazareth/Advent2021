# Problem: Giant Squid
# URL: https://adventofcode.com/2021/day/4
# Date: December 4th, 2021
# Author: Alex Nazareth

'''
Input
'''

import numpy as np
INFILE = r'day4_input'  # text file with input data provided by AoC2021
BOARD_SIZE = 5  # bingo board size, assumed square


class BingoSquare:
    def __init__(self, val):
        self.value = val
        self.marked = False

    def is_marked(self) -> bool:
        return self.marked

    def set_marked(self):
        self.marked = True

    def get_value(self):
        return self.value


class BingoBoard:
    def __init__(self, board_values: list):
        self.board = list()
        for row in board_values:
            temp_row = []
            for val in row:
                temp_row.append(BingoSquare(val))
            self.board.append(temp_row)
        self.board_width = BOARD_SIZE

    def __str__(self):
        result = ''
        for row in self.board:
            for sq in row:
                result += str(sq.value) + ','
            result += '\n'
        return result

    def has_bingo(self) -> bool:
        for row in self.board:
            if all_marked(row):
                return True
        for col in range(self.board_width):
            board_col = [self.board[i][col] for i in range(self.board_width)]
            if all_marked(board_col):
                return True
        return False

    def mark_square(self, drawn_val):
        for row in self.board:
            for sq in row:
                if sq.value == drawn_val:
                    sq.set_marked()

    def sum_unmarked(self) -> int:
        result = 0
        for row in self.board:
            for sq in row:
                if not sq.is_marked():
                    result += sq.value
        return result


def part1(data):
    nums_to_draw = [int(i) for i in data[0].split(',')]

    boards = list()
    r_idx = 1
    while r_idx < len(data) - BOARD_SIZE + 1:
        temp_board = [r.replace('  ', ' ').strip() for r in data[r_idx:r_idx + BOARD_SIZE]]
        temp = [list(map(int, r.split(' '))) for r in temp_board]
        boards.append(BingoBoard(temp))
        r_idx += BOARD_SIZE

    for i in nums_to_draw:
        for b in boards:
            b.mark_square(i)
            if b.has_bingo():
                return i * b.sum_unmarked()


def all_marked(bingo_row: list[BingoSquare]) -> bool:
    for sq in bingo_row:
        if not sq.is_marked():
            return False
    return True


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str, delimiter='\n')
    print(part1(raw_data))
