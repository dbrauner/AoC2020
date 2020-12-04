"""
Create a folder with name 'dayX' and save the input.txt for that day in the folder.
Copy this content as snippet and happy coding
Use SHIFT+CTRL+R to run the program.
"""
import os
import logging as log

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# use the toggle below to enable/disable log messages from the output
# log.disable(log.DEBUG)

def solution(puzzle_input):
    """
    solve here
    :param puzzle_input:
    :return:
    """
    puzzle_solution = ''
    return puzzle_solution


if __name__ == '__main__':
    day = os.getcwd()[os.getcwd().rindex('/') + 1:]
    log.warning(f'Start of the program for {day}')

    with open('input.txt', 'r') as f:
        puzzle_input = f.readlines()
    log.warning(puzzle_input)

    puzzle_solution = solution(puzzle_input)
    log.warning(puzzle_solution)

    log.warning(f'End of the program for {day}')