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
    for signals, outputs in all_data:
        disp_key = {k: set() for k in range(10)}
        for sig in signals:
            lsig = len(sig)
            fsig = frozenset(sig)
            if lsig == 2:
                disp_key[1].add(fsig)
            elif lsig == 3:
                disp_key[7].add(fsig)
            elif lsig == 4:
                disp_key[4].add(fsig)
            elif lsig == 5:
                disp_key[2].add(fsig)
                disp_key[3].add(fsig)
                disp_key[5].add(fsig)
            elif lsig == 6:
                disp_key[0].add(fsig)
                disp_key[6].add(fsig)
                disp_key[9].add(fsig)
            elif lsig == 7:
                disp_key[8].add(fsig)
            else:
                print(f'unrecognized signal {sig}')
        key4 = list(disp_key[4])[0]
        key7 = list(disp_key[7])[0]
        num_to_add = ''
        for out in outputs:
            lout = len(out)
            if lout == 2:
                num_to_add += '1'
            elif lout == 3:
                num_to_add += '7'
            elif lout == 4:
                num_to_add += '4'
            elif lout == 5:
                if key7.issubset(out):
                    num_to_add += '3'
                elif len(key4.intersection(out)) == 3:
                    num_to_add += '5'
                else:
                    num_to_add += '2'
            elif lout == 6:
                if key4.issubset(out):
                    num_to_add += '9'
                elif key7.issubset(out):
                    num_to_add += '0'
                else:
                    num_to_add += '6'
            elif lout == 7:
                num_to_add += '8'
            else:
                print(f'unrecognized output signal {out}')
        run_sum += int(num_to_add)
    return run_sum


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
