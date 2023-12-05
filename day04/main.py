from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Card:
    numbers_win: List[int]
    numbers: List[int]
    count: int = 1


def parse_file(path_to_file: str) -> Dict[int, Card]:
    cards = {}

    with open(path_to_file) as f:
        raw_data = [line.rstrip('\n') for line in f.readlines()]

    for line in raw_data:
        card, numbers = line.split(':')
        card_id = int(card[5:])
        win_nums, nums = numbers.split(' |')
        cards[card_id] = Card(
                numbers_win=[int(win_nums[i:i+3]) for i in range(0, len(win_nums), 3)],
                numbers=[int(nums[i:i+3]) for i in range(0, len(nums), 3)]
        )
    return cards


def part1(cards: Dict[int, Card]) -> int:
    total_points = 0
    for card in cards.values():
        card_points = 0
        for win_num in card.numbers_win:
            if win_num in card.numbers:
                if card_points == 0:
                    card_points = 1
                else:
                    card_points *= 2
        total_points += card_points

    return total_points


def part2(cards: Dict[int, Card]) -> int:
    for card_id, card in cards.items():
        card_points = 0
        for win_num in card.numbers_win:
            if win_num in card.numbers:
                card_points += 1

        right_border = min(len(cards.keys()), card_id+card_points)
        for i in range(card_id+1, right_border+1):
            cards[i].count += card.count

    return sum(card.count for card in cards.values())


if __name__ == '__main__':
    input_path = 'input.txt'
    scratchcards = parse_file(input_path)
    print('part1')
    print(part1(scratchcards))
    print('part2')
    print(part2(scratchcards))
