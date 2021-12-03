# Problem: Binary Diagnostic
# URL: https://adventofcode.com/2021/day/3
# Date: December 3rd, 2021
# Author: Alex Nazareth

'''
Input text file with binary number on each row.
Output product of two binary numbers calculated.
See part 1 and part 2 for different subproblems.
'''

import numpy as np
INFILE = r'day3_input'


def part1(data):
    '''
    Input list of binary numbers.
    Output product of "gamma rate" and "epsilon rate" where:
    -"gamma rate" defines each bit as most common bit in that position in the file.
    -"epsilon rate" is the same, but with LEAST common bit in each position.
    - e.g. for 001, 011, 001, we have gamma rate 001 and epsilon rate 110
-    output of this example is 1*8 = 8.
    :param data: list of strings
    :return: integer
    '''

    gamma_rate, epsilon_rate = 0, 0
    for bit_pos in range(len(data[0])):
        count_bits = {'0': 0, '1': 0}
        for row in data:
            count_bits[row[bit_pos]] += 1
        if count_bits['1'] > count_bits['0']:
            gamma_rate += 2**(len(data[0]) - bit_pos - 1)
        else:
            epsilon_rate += 2**(len(data[0]) - bit_pos - 1)
    return gamma_rate*epsilon_rate


def part2(data) -> int:
    '''
    Input list of binary numbers.
    Output product of "oxygen generator rating" and "CO2 scrubber rating" where:
    - both values defined by going through each bit position and discarding subset of numbers
    - for O2 rating, keep only numbers with most frequent bit in that position,
        keep 1's in case of tie
    - for CO2 rating, keep LESS frequent, keep 0's in case of tie
    :param data: list of strings
    :return: integer
    '''

    o2 = reduce(data, 0, keep=True)
    co2 = reduce(data, 0, keep=False)
    return int(o2, 2)*int(co2, 2)


def reduce(numbers, pos, keep):
    '''
    Recursive function to reduce list of values based on most common bit in
    position "pos".
    :param numbers: list of strings representing binary numbers
    :param pos: integer representing current bit position
    :param keep: boolean indicating if we keep the most common or discard
    :return: string representing final binary number after all reduction
    '''
    if len(numbers) == 1:
        return numbers[0]
    one_nums, zero_nums = [], []
    for n in numbers:
        if n[pos] == '1':
            one_nums.append(n)
        else:
            zero_nums.append(n)
    if len(one_nums) >= len(zero_nums):
        if keep:
            return reduce(one_nums, pos+1, keep)
        else:
            return reduce(zero_nums, pos+1, keep)
    else:
        if keep:
            return reduce(zero_nums, pos+1, keep)
        else:
            return reduce(one_nums, pos+1, keep)


if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str, delimiter='\n')
    print(part1(raw_data))
    print(part2(raw_data))
