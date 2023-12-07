from dataclasses import dataclass
from typing import List, Dict, Tuple


@dataclass
class Range:
    start: int
    end: int
    offset: int = 0


category = {
    'seed-to-soil': 0,
    'soil-to-fertilizer': 1,
    'fertilizer-to-water': 2,
    'water-to-light': 3,
    'light-to-temperature': 4,
    'temperature-to-humidity': 5,
    'humidity-to-location': 6,
}


def parse_file(path_to_file: str) -> Tuple[List, Dict[int, List[Range]]]:
    book: Dict[int, List[Range]] = {}

    with open(path_to_file) as f:
        raw_data = [line.rstrip('\n') for line in f.readlines()]

    seeds = [int(seed) for seed in raw_data[0].split(': ')[1].split(' ')]
    i = 2

    while i < len(raw_data):
        if raw_data[i] != '':
            type_data = category[raw_data[i].split(' ')[0]]
            book[type_data] = []
            i += 1

            while i < len(raw_data) and raw_data[i] != '':
                dest, source, length = raw_data[i].split(' ')
                book[type_data].append(
                    Range(
                        start=int(source),
                        end=int(source) + int(length) - 1,
                        offset=int(source) - int(dest)
                    )
                )
                i += 1

            book[type_data].sort(key=lambda x: x.start)
        i += 1
    return seeds, book


def part1(seeds: List, maps: Dict[int, List[Range]]) -> int:
    location = []
    for seed in seeds:
        for category_id in category.values():
            for comp in maps[category_id]:
                if comp.start <= seed <= comp.end:
                    seed -= comp.offset
                    break

        location.append(seed)
    return min(location)


def part2(seeds: List, maps: Dict[int, List[Range]]) -> int:
    location = []

    for j in range(0, len(seeds), 2):
        seed_range = [
            Range(
                start=seeds[j],
                end=seeds[j] + seeds[j+1],
            )
        ]

        for chapter in category.values():
            for page in maps[chapter]:
                for i in range(len(seed_range)):
                    if seed_range[i].offset != 0:
                        continue

                    if seed_range[i].start <= page.end and page.start <= seed_range[i].end:
                        if seed_range[i].start < page.start:
                            seed_range.append(
                                Range(
                                    start=seed_range[i].start,
                                    end=page.start - 1
                                )
                            )
                            seed_range[i].start = page.start

                        if page.end < seed_range[i].end:
                            seed_range.append(
                                Range(
                                    start=page.end + 1,
                                    end=seed_range[i].end
                                )
                            )
                            seed_range[i].end = page.end
                        seed_range[i].offset = page.offset

            for el in seed_range:
                el.start -= el.offset
                el.end -= el.offset
                el.offset = 0

        location.append(min([seed_range[i].start for i in range(len(seed_range))]))
    return min(location)


if __name__ == '__main__':
    input_path = 'input.txt'
    planting_seeds, almanac = parse_file(input_path)
    print('part1')
    print(part1(planting_seeds, almanac))
    print('part2')
    print(part2(planting_seeds, almanac))
