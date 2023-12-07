from dataclasses import dataclass
from typing import List


@dataclass
class Ride:
    time: int
    distance: int


def read_file(path_to_file: str) -> List:
    with open(path_to_file) as f:
        return [line.rstrip('\n') for line in f.readlines()]


def parse_multi_races(data: List) -> List[Ride]:
    rides = []
    parsed_data = [' '.join(line.split()).split(' ') for line in data]
    for i in range(1, len(parsed_data[0])):
        rides.append(
            Ride(
                time=int(parsed_data[0][i]),
                distance=int(parsed_data[1][i]),
            )
        )
    return rides


def parse_single_race(data: List) -> Ride:
    parsed_data = [''.join(line.split()).split(':') for line in data]
    ride = Ride(
        time=int(parsed_data[0][1]),
        distance=int(parsed_data[1][1]),
    )
    return ride


def part1(data: List) -> int:
    races = parse_multi_races(data)
    ways_to_win = 1
    for race in races:
        records = 0
        for i in range(race.time):
            if (race.time - i) * i > race.distance:
                records += 1
        ways_to_win *= records

    return ways_to_win


def part2(data: List) -> int:
    race = parse_single_race(data)
    return search_reverse(race) - search_forward(race) + 1


def search_forward(ride: Ride) -> int:
    for i in range(ride.time):
        if (ride.time - i) * i > ride.distance:
            return i


def search_reverse(ride: Ride) -> int:
    for i in range(ride.time, -1, -1):
        if (ride.time - i) * i > ride.distance:
            return i


if __name__ == '__main__':
    input_path = 'input.txt'
    input_data = read_file(input_path)
    print('part1')
    print(part1(input_data))
    print('part2')
    print(part2(input_data))
