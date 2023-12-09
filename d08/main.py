import math
from typing import Dict, Tuple


def parse_file(path_to_file: str) -> Tuple[str, Dict]:
    with open(path_to_file) as f:
        data = [line.rstrip('\n') for line in f.readlines()]

    nodes: Dict = {}
    instructions = data[0]
    for line in data[2:]:
        value, navigation = line.split(' = ')
        left, right = navigation[1:-1].split(', ')
        nodes[value] = {
            'L': left,
            'R': right
        }

    return instructions, nodes


def part1(instr: str, network: Dict) -> int:
    i, position, steps, instr_len = 0, 'AAA', 0, len(instr) - 1
    while not position == 'ZZZ':
        position = network[position][instr[i]]
        steps += 1
        if i == instr_len:
            i = 0
        else:
            i += 1

    return steps


def part2(instr: str, network: Dict) -> int:
    start_nodes = [pos for pos in network.keys() if pos[2] == 'A']
    steps_nodes = []
    for position in start_nodes:
        step, i, instr_len = 0, 0, len(instr) - 1
        while not position[2] == 'Z':
            position = network[position][instr[i]]
            step += 1
            if i == instr_len:
                i = 0
            else:
                i += 1
        steps_nodes.append(step)

    return math.lcm(*steps_nodes)


if __name__ == '__main__':
    input_path = 'input.txt'
    rules, navigation_data = parse_file(input_path)
    print('part1')
    print(part1(rules, navigation_data))
    print('part2')
    print(part2(rules, navigation_data))
