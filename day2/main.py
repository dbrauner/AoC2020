"""
Create a folder with name 'dayX' and save the input.txt for that day in the folder.
Copy this content as snippet and happy coding
Use SHIFT+CTRL+R to run the program.
"""
import os
import logging as log
import re

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# use the toggle below to enable/disable log messages from the output
# log.disable(log.DEBUG)

PART_TWO = True


def solution(puzzle_input):
    """
For example, suppose you have the following list:
```
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```
Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of
 times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a
  at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs
 at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

PART TWO:
Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
    """
    valid_passwords = 0
    for line in puzzle_input:
        search = re.compile(r'(\d+)-(\d+) (\w): (\w*)')
        groups = search.search(line)
        min, max, letter, password = groups.groups()
        if not PART_TWO:
            valid_passwords += validate_part_one(min, max, letter, password)
        else:
            valid_passwords += validate_part_two(min, max, letter, password)

    return valid_passwords


def validate_part_one(min, max, letter, password):
    occurrences = password.count(letter)
    if int(max) >= occurrences >= int(min):
        return 1
    return 0


def validate_part_two(first, second, letter, password):
    if (password[int(first) - 1] == letter) != (password[int(second) - 1] == letter):
        return 1
    return 0


if __name__ == '__main__':
    day = os.getcwd()[os.getcwd().rindex('/') + 1:]
    log.warning(f'Start of the program for {day}')

    with open('input.txt', 'r') as f:
        puzzle_input = f.readlines()
    log.warning(puzzle_input)

    puzzle_solution = solution(puzzle_input)
    log.warning(puzzle_solution)

    log.warning(f'End of the program for {day}')
