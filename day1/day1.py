# Problem: Sonar Sweep
# URL: https://adventofcode.com/2021/day/1
# Date: December 1st, 2021
# Author: Alex Nazareth

'''
Input text file with one integer on each line, n-many lines.
Output number of integers which increase from the previous integer.
Eg. Max output n-1, in case of all numbers increasing.
For second part, compare rolling sums for increase, with a window of 3.
i.e. Is sum of 2nd, 3rd, 4th integers greater than the sum of 1st + 2nd + 3rd?
    And so on, until the (n-2)th, (n-1)th, and nth.
Note first part same as second part, only with window size 1 instead of 3.
'''


import numpy as np

INFILE = r'day1/day1_input'


def part2(w_size):
    in_data = np.loadtxt(INFILE, dtype=int, delimiter='\n')

    prev = sum(in_data[0:w_size])
    counter = 0
    i = w_size
    for val in in_data[w_size:]:
        rollsum = sum(in_data[i-w_size+1:i+1])
        if rollsum > prev:
            counter += 1
        prev = rollsum
        i += 1
    return counter


if __name__ == '__main__':
    print("The number of increases in seafloor elevation is: %d." % part2(1))
    print("When considering the sum of the last 3 data points, "
          "the number of increases in seafloor elevation is: %d." % part2(3))
