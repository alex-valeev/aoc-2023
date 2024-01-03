from typing import List
from dataclasses import dataclass
from copy import copy


@dataclass()
class Coord:
    x: int = 0
    y: int = 0


@dataclass(frozen=True)
class Impulse:
    x: int = 0
    y: int = 0

    def __len__(self):
        return 1


up = Impulse(y=-1)
down = Impulse(y=1)
left = Impulse(x=-1)
right = Impulse(x=1)

items = {
    '|': {
        up: up,
        down: down,
        left: [up, down],
        right: [up, down],
    },
    '-': {
        up: [left, right],
        down: [left, right],
        left: left,
        right: right,
    },
    '/': {
        up: right,
        down: left,
        left: down,
        right: up,
    },
    '\\': {
        up: left,
        down: right,
        left: up,
        right: down,
    },
    '.': {
        up: up,
        down: down,
        left: left,
        right: right,
    }
}


def parse_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [list(line.rstrip('\n')) for line in f.readlines()]


def energized_tiles(init_coord: Coord(), init_impulse: Impulse(), data: List) -> int:
    height, width = len(data), len(data[0])
    path = [['.'] * width for _ in range(height)]

    starts = [[init_coord, init_impulse]]
    for start in starts:
        position, impulse = start[0], start[1]
        for _ in range(height * width):
            if position.x < 0 or position.x > width - 1 or position.y < 0 or position.y > height - 1:
                break
            
            if path[position.y][position.x] == impulse:
                break
            else:
                path[position.y][position.x] = impulse
            
            pos_item = data[position.y][position.x]
            impulse = items[pos_item][impulse]
            if len(impulse) == 1:
                position.x += impulse.x
                position.y += impulse.y
            else:
                starts.append([copy(position), impulse[1]])
                position.x += impulse[0].x
                position.y += impulse[0].y
                impulse = impulse[0]

    return height * width - sum(row.count('.') for row in path)


def part1(data: List) -> int:
    return energized_tiles(Coord(0, 0), right, data)


def part2(data: List) -> int:
    total_tiles, height, width = [], len(data), len(data[0])
    for i in range(height):
        total_tiles.append(
            energized_tiles(
                Coord(i, 0),
                down,
                data
            )
        )
        total_tiles.append(
            energized_tiles(
                Coord(i, width - 1),
                up,
                data
            )
        )
    for j in range(width):
        total_tiles.append(
            energized_tiles(
                Coord(0, j),
                right,
                data
            )
        )
        total_tiles.append(
            energized_tiles(
                Coord(height - 1, j),
                left,
                data
            )
        )
    
    return max(total_tiles)


if __name__ == '__main__':
    input_path = 'input.txt'
    floor = parse_file(input_path)
    print('part1')
    print(part1(floor))
    print('part2')
    print(part2(floor))
