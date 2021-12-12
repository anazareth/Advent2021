# Problem: Seven Segment Search
# URL: https://adventofcode.com/2021/day/8
# Date: December 8th, 2021
# Author: Alex Nazareth

"""
Repairing seven segment digit display, segments 'a' through 'g' as follows:
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
"""

import numpy as np
INFILE = r'day8_input'  # text file with input data provided by AoC2021


def part1(output_only):
    easy_digit_lengths = [2, 4, 3, 7]  # number of segments for digits 1, 4, 7, 8
    count = 0
    for sig in output_only:
        if len(sig) in easy_digit_lengths:
            count += 1
    return count


def part2(all_data):
    run_sum = 0
    digit_signals = {'abcefg': 0, 'cf': 1,
                     'acdeg': 2, 'acdfg': 3,
                     'bcdf': 4, 'abdfg': 5,
                     'abdefg': 6, 'acf': 7,
                     'abcdefg': 8, 'abcdfg': 9}
    for row in all_data:
        num_segments = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        char_map = dict.fromkeys(num_segments, set(num_segments))  # key, value is new, old
        all_digits = range(0, 10)
        digit_possibilities = {k: set() for k in all_digits}

        all_signals = [s for grp in row for s in grp]
        for sig in all_signals:
            if len(sig) == 2:
                digit_possibilities[1].add(frozenset(sig))
            elif len(sig) == 3:
                digit_possibilities[7].add(frozenset(sig))
            elif len(sig) == 4:
                digit_possibilities[4].add(frozenset(sig))
            elif len(sig) == 5:
                digit_possibilities[2].add(frozenset(sig))
                digit_possibilities[3].add(frozenset(sig))
                digit_possibilities[5].add(frozenset(sig))
            elif len(sig) == 6:
                digit_possibilities[0].add(frozenset(sig))
                digit_possibilities[6].add(frozenset(sig))
                digit_possibilities[9].add(frozenset(sig))
            elif len(sig) == 7:
                digit_possibilities[8].add(frozenset(sig))
            else:
                print(f'Unrecognized signal {sig}.')

        letter_sets = []
        for i in all_digits:
            print(i)
            letter_sets.append(set([c for s in digit_possibilities[i] for c in s]))

        for c in num_segments:
            if all([c in letter_sets[0], c not in letter_sets[1], c in letter_sets[2],
                    c in letter_sets[3], c not in letter_sets[4], c in letter_sets[5],
                    c in letter_sets[6], c in letter_sets[7], c in letter_sets[8],
                    c in letter_sets[9]]):
                char_map[c] = 'a'
            elif all([c in letter_sets[0], c not in letter_sets[1], c not in letter_sets[2],
                      c not in letter_sets[3], c in letter_sets[4], c in letter_sets[5],
                      c in letter_sets[6], c not in letter_sets[7], c in letter_sets[8],
                      c in letter_sets[9]]):
                char_map[c] = 'b'
            elif all([c in letter_sets[0], c in letter_sets[1], c in letter_sets[2],
                      c in letter_sets[3], c in letter_sets[4], c not in letter_sets[5],
                      c not in letter_sets[6], c in letter_sets[7], c in letter_sets[8],
                      c in letter_sets[9]]):
                char_map[c] = 'c'
            elif all([ c not in letter_sets[0], c not in letter_sets[1], c in letter_sets[2],
                       c in letter_sets[3], c in letter_sets[4], c in letter_sets[5],
                       c in letter_sets[6], c not in letter_sets[7], c in letter_sets[8],
                       c in letter_sets[9]]):
                char_map[c] = 'd'
            elif all([c in letter_sets[0], c not in letter_sets[1], c in letter_sets[2],
                      c not in letter_sets[3], c not in letter_sets[4], c not in letter_sets[5],
                      c in letter_sets[6], c not in letter_sets[7], c in letter_sets[8],
                      c not in letter_sets[9]]):
                char_map[c] = 'e'
            elif all([c not in letter_sets[0], c in letter_sets[1], c in letter_sets[2],
                      c in letter_sets[3], c in letter_sets[4], c in letter_sets[5],
                      c in letter_sets[6], c in letter_sets[7], c in letter_sets[8],
                      c in letter_sets[9]]):
                char_map[c] = 'f'
            elif all([c in letter_sets[0], c not in letter_sets[1], c in letter_sets[2],
                      c in letter_sets[3], c not in letter_sets[4], c in letter_sets[5],
                      c in letter_sets[6], c not in letter_sets[7], c in letter_sets[8],
                      c in letter_sets[9]]):
                char_map[c] = 'g'
            else:
                print(f'something bad for char {c}!!!')
        # translate output
        for o in row[1]:
            run_sum += digit_signals[trans_output(o, char_map)]
    return run_sum

def trans_output(text, char_mapping):
    result = ''
    for c in text:
        result += char_mapping[c]
    return ''.join(sorted(result))

if __name__ == '__main__':
    raw_data = np.loadtxt(INFILE, dtype=str, delimiter='\n')
    # output_values = [signal for r in raw_data for signal in r.split('|')[1].split(' ')
    #                  if signal not in {'|', ''}]
    split_point = 10

    parsed_rows = []  # list of tuples (10 signals, 4 output digits)
    for r in raw_data:
        s, o = r.split(' ')[:split_point], r.split(' ')[split_point+1:]
        parsed_rows.append((s, o))
    output_values = [o for (s, o) in parsed_rows]
    output_values2 = [s for signals in output_values for s in signals ]

    print(f'The number of times digits 1, 4, 7, 8 appear is: {part1(output_values2)}')
    print(f'The sum of all output values is: {part2(parsed_rows)}')
