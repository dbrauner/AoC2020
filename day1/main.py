"""
Create a folder with name 'dayX' and save the input.txt for that day in the folder.
Copy this content as snippet and happy coding
Use SHIFT+CTRL+R to run the program.
"""
import os
import logging as log
import itertools

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# use the toggle below to enable/disable log messages from the output
# log.disable(log.DEBUG)
PART_TWO = True

def solution(puzzle_input):
    """
Before you leave, the Elves in accounting just need you to fix your expense report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299. Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

Of course, your expense report is much larger. Find the two entries that sum to 2020; what do you get if you multiply them together?


    """
    numbers = [int(k) for k in puzzle_input]
    for p in itertools.combinations(numbers, 2):
        if (p[0] + p[1]) == 2020:
            log.debug('Found 2020')
            result_part_one = p[0] * p[1]
    if not PART_TWO:
        return result_part_one

    for p in itertools.combinations(numbers, 3):
        if (p[0] + p[1] + p[2]) == 2020:
            log.debug('Found 2020')
            result_part_two = p[0] * p[1] * p[2]
            log.debug(f'[Part Two] {result_part_two}')

if __name__ == '__main__':
    day = os.getcwd()[os.getcwd().rindex('/') + 1:]
    log.warning(f'Start of the program for {day}')

    with open('input.txt', 'r') as f:
        puzzle_input = f.readlines()
    log.warning(puzzle_input)

    puzzle_solution = solution(puzzle_input)
    log.warning(f'[Part One] {puzzle_solution}')

    log.warning(f'End of the program for {day}')