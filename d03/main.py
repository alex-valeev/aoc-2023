from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Part:
    part_number: int
    x_start: int
    x_end: int
    y: int


@dataclass
class Symbol:
    x: int
    y: int
    is_star: bool


def parse_file(path_to_file: str) -> Tuple[List[Part], List[Symbol]]:
    symbols, parts = [], []

    with open(path_to_file) as f:
        raw_data = [line.rstrip('\n') for line in f.readlines()]

    rows = len(raw_data)
    columns = len(raw_data[0])

    for y in range(rows):
        x = 0
        while x < columns:
            if raw_data[y][x].isdigit():
                x_end = x + 1
                while x_end < columns:
                    if not raw_data[y][x_end].isdigit():
                        break
                    x_end += 1
                parts.append(
                    Part(
                        part_number=int(raw_data[y][x:x_end]),
                        x_start=x,
                        x_end=x_end - 1,
                        y=y
                    )
                )
                x = x_end
                if x == columns:
                    break
            if raw_data[y][x] != '.':
                symbols.append(
                    Symbol(
                        x=x,
                        y=y,
                        is_star=True if raw_data[y][x] == '*' else False
                    )
                )
            x += 1

    return parts, symbols


def part1(parts: List[Part], symbols: List[Symbol]) -> int:
    total_parts_num = 0
    for part in parts:
        for symbol in symbols:
            if (abs(symbol.x - part.x_start) <= 1 or abs(symbol.x - part.x_end) <= 1) \
                    and abs(symbol.y - part.y) <= 1:
                total_parts_num += part.part_number
                break
    return total_parts_num


def part2(parts: List[Part], symbols: List[Symbol]) -> int:
    total_parts_num = 0
    for symbol in symbols:
        if not symbol.is_star:
            continue
        parts_count, parts_sum = 0, 1
        for part in parts:
            if (abs(symbol.x - part.x_start) <= 1 or abs(symbol.x - part.x_end) <= 1) \
                    and abs(symbol.y - part.y) <= 1:
                parts_count += 1
                parts_sum *= part.part_number
        if parts_count > 1:
            total_parts_num += parts_sum
    return total_parts_num


if __name__ == '__main__':
    input_path = 'input.txt'
    part_numbers, mystery_symbols = parse_file(input_path)
    print('part1')
    print(part1(part_numbers, mystery_symbols))
    print('part2')
    print(part2(part_numbers, mystery_symbols))
