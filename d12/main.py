from typing import List
from functools import cache


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        text = [line.rstrip('\n').split(' ') for line in f.readlines()]

    for i in range(len(text)):
        text[i][1] = [int(el) for el in text[i][1].split(',')]

    return text


def calculating(symbols: str, sequence: List[int]) -> int:
    @cache
    def recurs(sym: int, seq: int) -> int:
        ret = 0
        if seq == len(sequence):
            return 1

        if sym == len(symbols):
            return 0

        if symbols[sym] in '.?':
            ret += recurs(sym + 1, seq)

        group_size = sym + sequence[seq]
        if group_size < len(symbols):
            if '.' not in symbols[sym:group_size]:
                if seq == len(sequence) - 1 and '#' in symbols[group_size:]:
                    return ret
                if symbols[group_size] != '#':
                    ret += recurs(group_size + 1, seq + 1)
        return ret

    return recurs(0, 0)


def part1(data: List) -> int:
    total_combinations = 0
    for line in data:
        springs, groups = line[0] + '?', line[1]
        total_combinations += calculating(symbols=springs, sequence=groups)

    return total_combinations


def part2(data: List) -> int:
    total_combinations = 0
    for line in data:
        springs, groups = (line[0] + '?') * 5, line[1] * 5
        total_combinations += calculating(symbols=springs, sequence=groups)

    return total_combinations


if __name__ == '__main__':
    input_path = 'input.txt'
    hot_springs = parse_file(input_path)
    print('part1')
    print(part1(hot_springs))
    print('part2')
    print(part2(hot_springs))
