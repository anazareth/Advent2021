# Problem: Giant Squid
# URL: https://adventofcode.com/2021/day/4
# Date: December 4th, 2021
# Author: Alex Nazareth

"""
Bingo game with a multi-armed giant squid.
"""

import numpy as np
INFILE = r'day4_input'  # text file with input data provided by AoC2021
BOARD_SIZE = 5  # bingo board size, assumed square


class BingoSquare:
    """
    Object representing square tile on a Bingo board, has a numeric value and
    boolean marked if the number was drawn in the game.
    """
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
    """
    Object representing a Bingo board made up of BingoSquare objects.
    """
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
            if self.all_marked(row):
                return True
        for col in range(self.board_width):
            board_col = [self.board[i][col] for i in range(self.board_width)]
            if self.all_marked(board_col):
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

    @staticmethod
    def all_marked(bingo_row: list[BingoSquare]) -> bool:
        for sq in bingo_row:
            if not sq.is_marked():
                return False
        return True


def part1(nums_to_draw, boards) -> int:
    """
    Draw numbers one by one from list, marking squares on all bingo boards with
    that number. Stop when a board wins by having a row or column fully marked.
    :param nums_to_draw: list of int, bingo numbers drawn in order
    :param boards: list of BingoBoard objects
    :return: int, product of last drawn number from list multiplied by sum
                of unmarked squares on first winning board
    """

    for i in nums_to_draw:
        for b in boards:
            b.mark_square(i)
            if b.has_bingo():
                return i * b.sum_unmarked()


def part2(nums_to_draw, boards) -> int():
    """
    Draw numbers one by one from list, marking squares on all bingo boards with
    that number. Stop when all-but-one boards have "won", i.e. find final board
    without a fully marked row or column.
    :param nums_to_draw: list of int, bingo numbers drawn in order
    :param boards: list of BingoBoard objects
    :return: int, product of last drawn number from list multiplied by sum
                of unmarked squares on final winning board
    """

    remaining_boards = set(range(len(boards)))  # index in list 'boards'
    for i in nums_to_draw:
        for b_idx, b in enumerate(boards):
            b.mark_square(i)
            if b.has_bingo():
                remaining_boards.discard(b_idx)
                if len(remaining_boards) == 0:
                    return i * b.sum_unmarked()


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str, delimiter='\n')

    nums = [int(i) for i in raw_data[0].split(',')]

    boards_list = list()
    r_idx = 1
    while r_idx < len(raw_data) - BOARD_SIZE + 1:
        temp_board = [r.replace('  ', ' ').strip() for r in raw_data[r_idx:r_idx + BOARD_SIZE]]
        temp = [list(map(int, r.split(' '))) for r in temp_board]
        boards_list.append(BingoBoard(temp))
        r_idx += BOARD_SIZE

    print(f'Solution to part 1: {part1(nums, boards_list)}')
    print(f'Solution to part 2: {part2(nums, boards_list)}')

