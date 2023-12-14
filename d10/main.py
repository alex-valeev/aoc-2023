from copy import copy
from typing import List, Tuple, Dict
from dataclasses import dataclass


@dataclass
class Coord:
    x: int = 0
    y: int = 0


@dataclass
class MazeSymbol:
    input_impulse: List[Coord]
    changing_impulse: Coord()


@dataclass
class Directions:
    left = Coord(x=-1)
    right = Coord(x=1)
    up = Coord(y=-1)
    down = Coord(y=1)


moves: Dict[str, MazeSymbol] = {
    '|': MazeSymbol(
        input_impulse=[
            Directions.up,
            Directions.down
        ],
        changing_impulse=Coord()
    ),
    '-': MazeSymbol(
        input_impulse=[
            Directions.left,
            Directions.right
        ],
        changing_impulse=Coord()
    ),
    'L': MazeSymbol(
        input_impulse=[
            Directions.down,
            Directions.left
        ],
        changing_impulse=Coord(x=1, y=-1),
    ),
    'J': MazeSymbol(
        input_impulse=[
            Directions.right,
            Directions.down
        ],
        changing_impulse=Coord(x=-1, y=-1),
    ),
    '7': MazeSymbol(
        input_impulse=[
            Directions.right,
            Directions.up
        ],
        changing_impulse=Coord(x=-1, y=1),
    ),
    'F': MazeSymbol(
        input_impulse=[
            Directions.left,
            Directions.up,
        ],
        changing_impulse=Coord(x=1, y=1),
    ),
    '.': MazeSymbol(
        input_impulse=[],
        changing_impulse=Coord()
    ),
    'S': MazeSymbol(
        input_impulse=[
            Directions.left,
            Directions.right,
            Directions.down,
            Directions.up,
        ],
        changing_impulse=Coord()
    ),
}


def parse_file(path_to_file: str) -> Tuple[Coord, List[List[str]]]:
    with open(path_to_file) as f:
        lines = [list(line.rstrip('\n')) for line in f.readlines()]
    start_position = Coord()
    for i in range(len(lines)):
        if 'S' in lines[i]:
            start_position.y = i
            start_position.x = lines[i].index('S')
            break

    borders = Coord(x=len(lines), y=len(lines[0]))
    impulses = start_impulses(start=start_position, borders=borders)
    for impulse in impulses:
        bends = find_corners(copy(start_position), impulse, lines)
        if len(bends) > 0:
            break

    return bends


def start_impulses(start: Coord, borders: Coord) -> List[Coord]:
    start_points = []
    for x in range(start.x - 1, start.x + 2, 2):
        if 0 <= x < borders.x:
            start_points.append(
                Coord(x=x - start.x)
            )
    for y in range(start.y - 1, start.y + 2, 2):
        if 0 <= y < borders.y:
            start_points.append(
                Coord(y=y - start.y)
            )

    return start_points


def find_corners(start: Coord, impulse: Coord, maze: List[List[str]]) -> List[Coord]:
    bends = [copy(start)]
    while True:
        start.x += impulse.x
        start.y += impulse.y

        maze_element = maze[start.y][start.x]

        if impulse not in moves[maze_element].input_impulse:
            return []

        match maze_element:
            case '.':
                return []
            case 'S':
                break
            case 'L' | 'J' | 'F' | '7':
                bends.append(copy(start))

        impulse.x += moves[maze[start.y][start.x]].changing_impulse.x
        impulse.y += moves[maze[start.y][start.x]].changing_impulse.y
        bends.append(copy(start))

    bends.append(copy(start))
    return bends


def calc_path(turns: List[Coord]) -> int:
    return sum(abs(turns[i].x + turns[i].y - turns[i + 1].x - turns[i + 1].y) for i in range(len(turns) - 1))


def part1(bends: List[Coord]) -> int:
    return calc_path(bends) // 2


def part2(bends: List[Coord]) -> int:
    left, right = 0, 0
    for i in range(len(bends) - 1):
        left += bends[i].x * bends[i + 1].y
        right += bends[i].y * bends[i + 1].x

    return (abs(left - right) - calc_path(bends)) // 2 + 1


if __name__ == '__main__':
    input_path = 'input.txt'
    corners = parse_file(input_path)
    print('part1')
    print(part1(corners))
    print('part2')
    print(part2(corners))
