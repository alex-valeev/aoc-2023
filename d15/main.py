from typing import List, Dict
from collections import defaultdict


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n').split(',') for line in f.readlines()][0]


def hash_algorithm(line: str) -> int:
    ret = 0
    for el in line:
        ret += ord(el)
        ret *= 17
        ret %= 256

    return ret


def part1(data: List) -> int:
    total = 0
    for step in data:
        total += hash_algorithm(step)

    return total


def part2(data: List) -> int:
    total = 0
    boxes = defaultdict(lambda: defaultdict(int))
    for step in data:
        if step[-2] == '=':
            box_num = hash_algorithm(step[:-2])
            boxes[box_num][step[:-2]] = int(step[-1])
        else:
            box_num = hash_algorithm(step[:-1])
            if step[:-1] in boxes[box_num]:
                del boxes[box_num][step[:-1]]

    for num, box in boxes.items():
        for slot, focal_length in enumerate(box.values()):
            total += (num + 1) * (slot + 1) * focal_length

    return total


if __name__ == '__main__':
    input_path = 'input.txt'
    init_sequence = parse_file(input_path)
    print('part1')
    print(part1(init_sequence))
    print('part2')
    print(part2(init_sequence))
