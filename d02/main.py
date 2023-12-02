from math import prod


def read_file(path_to_file: str) -> list:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def part1(path: str) -> int:
    data = read_file(path)
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    sum_ids = 0

    for line in data:
        impossible = False
        game = line.split(': ')

        for handful in game[1].replace(',', ';').split('; '):
            el = handful.split(' ')
            if bag[el[1]] < int(el[0]):
                impossible = True
                break

        if not impossible:
            sum_ids += int(game[0].split(' ')[1])

    return sum_ids


def part2(path: str) -> int:
    data = read_file(path)
    sum_power = 0

    for line in data:
        bag = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        game = line.split(': ')

        for handful in game[1].replace(',', ';').split('; '):
            el = handful.split(' ')
            if bag[el[1]] < int(el[0]):
                bag[el[1]] = int(el[0])
        sum_power += prod(bag.values())

    return sum_power


if __name__ == '__main__':
    input_path = 'input.txt'
    print('part1')
    print(part1(input_path))
    print('part2')
    print(part2(input_path))