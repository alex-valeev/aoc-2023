def read_file(path_to_file: str) -> list:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def part1(path: str) -> int:
    calibration_value = 0
    text = read_file(path)

    for line in text:
        digits = [int(el) for el in line if el.isdigit()]
        if len(digits) > 0:
            calibration_value += digits[0] * 10 + digits[-1]

    return calibration_value


def part2(path: str) -> int:
    calibration_value = 0
    text = read_file(path)
    text_digits = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    for line in text:
        digits = []
        for i in range(len(line)):
            if line[i].isdigit():
                digits.append(int(line[i]))
            else:
                for key, val in text_digits.items():
                    if line[i:].startswith(val):
                        digits.append(key)
                        break
        if len(digits) > 0:
            calibration_value += digits[0] * 10 + digits[-1]

    return calibration_value


if __name__ == '__main__':
    input_path = 'test2.txt'
    print('part1')
    print(part1(input_path))
    print('part2')
    print(part2(input_path))
