from typing import List


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def move_rock(line: List[str]) -> List[str]:
    line_size = len(line)
    for i in range(line_size - 1, -1, -1):
        if line[i] == 'O':
            for j in range(i + 1, line_size):
                if line[j] != '.':
                    line[i], line[j - 1] = line[j - 1], line[i]
                    break
                if j == line_size - 1:
                    line[i], line[j] = line[j], line[i]

    for el in line:
        yield el


def move_circle(height, width, data: List) -> List:
    # move north
    for x in range(width):
        k = height - 1
        for el in move_rock([data[y][x] for y in range(height)][::-1]):
            data[k][x] = el
            k -= 1

    # move west
    for y in range(height):
        k = width - 1
        for el in move_rock([data[y][x] for x in range(width)][::-1]):
            data[y][k] = el
            k -= 1

    # move south
    for x in range(width):
        k = 0
        for el in move_rock([data[y][x] for y in range(height)]):
            data[k][x] = el
            k += 1

    # move east
    for y in range(height):
        k = 0
        for el in move_rock([data[y][x] for x in range(width)]):
            data[y][k] = el
            k += 1

    return data


def part1(data: List) -> int:
    width, height = len(data[0]), len(data)

    for x in range(width):
        j = height - 1
        for el in move_rock([data[y][x] for y in range(height)][::-1]):
            data[j][x] = el
            j -= 1

    total = 0
    for i in range(height):
        total += data[i].count('O') * (height - i)

    return total


def part2(data: List) -> int:
    cycles = (1000000000 - 97) % 36 + 97
    width, height = len(data[0]), len(data)

    for i in range(cycles):
        data = move_circle(height, width, data)

    total = 0
    for i in range(height):
        total += data[i].count('O') * (height - i)

    return total


if __name__ == '__main__':
    input_path = 'input.txt'
    reflector = read_file(input_path)
    print('part1')
    print(part1(reflector))
    print('part2')
    print(part2(reflector))
