from typing import List


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        text = [line.rstrip('\n') for line in f.readlines()]
        return [[int(el) for el in line.split(' ')] for line in text]


def build_sequence(history: List[int]) -> List[List[int]]:
    sequence = [history]
    for i in range(0, len(history) - 1):
        sequence.append(
            [sequence[i][j] - sequence[i][j - 1] for j in range(1, len(sequence[-1]))]
        )
        if sum(sequence[i]) == 0:
            break
    return sequence


def part1(data: List[str]) -> int:
    total_extrapolated = 0
    for line in data:
        predict = build_sequence(line)
        extrapolation = 0
        for i in range(len(predict)-2, -1, -1):
            extrapolation += predict[i][-1]
        total_extrapolated += extrapolation
    return total_extrapolated


def part2(data: List[str]) -> int:
    total_extrapolated = 0
    for line in data:
        predict = build_sequence(line)
        extrapolation = 0
        for i in range(len(predict)-2, -1, -1):
            extrapolation = predict[i][0] - extrapolation
        total_extrapolated += extrapolation
    return total_extrapolated


if __name__ == '__main__':
    input_path = 'input.txt'
    input_data = read_file(input_path)
    print('part1')
    print(part1(input_data))
    print('part2')
    print(part2(input_data))
