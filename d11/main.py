from typing import List, Tuple
from dataclasses import dataclass, field


@dataclass
class Coord:
    x: int = 0
    y: int = 0


@dataclass
class Expansion:
    x: List = field(default_factory=lambda: [])
    y: List = field(default_factory=lambda: [])


def read_file(path_to_file: str) -> Tuple[Expansion, List[Coord]]:
    with open(path_to_file) as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    expansion = Expansion()
    height = len(lines)
    for i in range(height - 1, -1, -1):
        if '#' not in lines[i]:
            expansion.y.append(i)

    width, height = len(lines[0]), len(lines)
    for j in range(width - 1, -1, -1):
        if all(lines[i][j] == '.' for i in range(height)):
            expansion.x.append(j)

    universe = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                universe.append(
                    Coord(
                        y=i,
                        x=j,
                    )
                )

    return expansion, universe


def sum_paths(exp: Expansion, galax: List[Coord], multiply: int) -> int:
    total_short_path = 0
    for i in range(len(galax)):
        for j in range(i+1, len(galax)):
            gravity = sum(1 for el in exp.x if galax[i].x < el < galax[j].x or galax[j].x < el < galax[i].x) +\
                      sum(1 for el in exp.y if galax[i].y < el < galax[j].y or galax[j].y < el < galax[i].y)
            total_short_path += abs(galax[i].y - galax[j].y) + abs(galax[i].x - galax[j].x) + gravity * (multiply - 1)
    return total_short_path


def part1(expansion: Expansion, universe: List[Coord]) -> int:
    expand_coefficient = 2
    return sum_paths(expansion, universe, expand_coefficient)


def part2(expansion: Expansion, universe: List[Coord]) -> int:
    expand_coefficient = 1000000
    return sum_paths(expansion, universe, expand_coefficient)


if __name__ == '__main__':
    input_path = 'input.txt'
    space, galaxies = read_file(input_path)
    print('part1')
    print(part1(space, galaxies))
    print('part2')
    print(part2(space, galaxies))
