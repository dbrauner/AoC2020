"""
the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.


"""
import os
import logging as log

PART_TWO = True

log.basicConfig(level=log.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# use the toggle below to enable/disable log messages from the output
# log.disable(log.DEBUG)

def solution(puzzle_input):

    trees_a = 0
    trees_b = 0
    trees_c = 0
    trees_d = 0
    trees_e = 0
    index_a = 0
    index_b = 0
    index_c = 0
    index_d = 0
    index_e = 0
    for i in range(1, len(puzzle_input)):
        index_a += 1
        if puzzle_input[i][index_a % len(puzzle_input[i])] == '#':
            trees_a +=1
        index_b += 3
        if puzzle_input[i][index_b % len(puzzle_input[i])] == '#':
            trees_b += 1

        index_c += 5
        if puzzle_input[i][index_c % len(puzzle_input[i])] == '#':
            trees_c +=1
        index_d += 7
        if puzzle_input[i][index_d % len(puzzle_input[i])] == '#':
            trees_d +=1
        if i % 2 == 0:
            index_e += 1
            if puzzle_input[i][index_e % len(puzzle_input[i])] == '#':
                trees_e += 1

    if not PART_TWO:
        return trees_b
    else:
        return trees_a * trees_b * trees_c * trees_d * trees_e




    """
    solve here
    :param puzzle_input:
    :return:
    """

if __name__ == '__main__':
    day = os.getcwd()[os.getcwd().rindex('/') + 1:]
    log.warning(f'Start of the program for {day}')

    puzzle_input = []
    with open('input.txt', 'r') as f:
        for line in f:
            puzzle_input.append(line.strip())
    log.warning(puzzle_input)

    puzzle_solution = solution(puzzle_input)
    log.warning(puzzle_solution)

    log.warning(f'End of the program for {day}')