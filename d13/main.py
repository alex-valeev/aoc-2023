from typing import List
from itertools import groupby
from copy import copy


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        text = [line.rstrip('\n') for line in f.readlines()]

    return [list(group) for key, group in groupby(text, key=lambda x: x == '') if not key]


def transpose(data: List) -> List:
    width, height = len(data[0]), len(data)
    t_data = []
    for y in range(width):
        t_data.append('')
        for x in range(height):
            t_data[y] += data[x][y]

    return t_data


def diff_str(str1: str, str2: str) -> int:
    return sum(1 if s1 != s2 else 0 for s1, s2 in zip(str1, str2))


def find_reflection_clear(data: List) -> int:
    for i in range(len(data)):
        if data[i] in data[i + 1:]:
            edge_reflection = data[i + 1:].index(data[i])
            center_reflection = (edge_reflection + 1) // 2 + i + 1
            is_ok = True
            for j in range(min(center_reflection, len(data) - center_reflection)):
                if data[center_reflection - j - 1] != data[center_reflection + j]:
                    is_ok = False
                    break
            if is_ok:
                return center_reflection

    return 0


def find_reflection_smudge(data: List) -> int:
    for i in range(len(data) - 1):
        for j in range(i + 1, len(data)):
            if diff_str(data[i], data[j]) == 1:
                if (i + j) % 2 == 0:
                    continue
                new_data = copy(data)
                new_data[i] = new_data[j]
                center_reflection = (j - i - 1) // 2 + i + 1
                is_ok = True
                for j in range(min(center_reflection, len(new_data) - center_reflection)):
                    if new_data[center_reflection - j - 1] != new_data[center_reflection + j]:
                        is_ok = False
                        break
                if is_ok:
                    return center_reflection

    return 0


def part1(data: List) -> int:
    total = 0
    for i in range(len(data)):
        total += find_reflection_clear(data[i]) * 100 + find_reflection_clear(transpose(data[i]))

    return total


def part2(data: List) -> int:
    total = 0
    for i in range(len(data)):
        total += find_reflection_smudge(data[i]) * 100 + find_reflection_smudge(transpose(data[i]))

    return total


if __name__ == '__main__':
    input_path = 'input.txt'
    mirrors = parse_file(input_path)
    print('part1')
    print(part1(mirrors))
    print('part2')
    print(part2(mirrors))
