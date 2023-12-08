from dataclasses import dataclass, field
from typing import List
from collections import defaultdict


@dataclass
class Hand:
    cards: str
    bid: int
    strength: List[int] = field(default_factory=lambda: [])
    hand_type: int = 0


strength_card_part1 = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
}

strength_card_part2 = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
}

hand_types = {
    '11111': 1,
    '2111': 2,
    '221': 3,
    '311': 4,
    '32': 5,
    '41': 6,
    '5': 7,
}

joker = 'J'


def element_counter(elements: str) -> str:
    symbols = defaultdict(int)
    for el in elements:
        symbols[el] += 1

    return ''.join(sorted([str(sym) for sym in symbols.values()], reverse=True))


def element_counter_with_joker(elements: str) -> str:
    symbols, j_card = defaultdict(int), 0
    for el in elements:
        if el == joker:
            j_card += 1
        else:
            symbols[el] += 1

    if len(symbols) == 0:
        symbols[joker] = j_card
    else:
        symbols[max(symbols, key=symbols.get)] += j_card

    return ''.join(sorted([str(sym) for sym in symbols.values()], reverse=True))


def parse_file(path_to_file: str) -> List[Hand]:
    with open(path_to_file) as f:
        data = [line.rstrip('\n') for line in f.readlines()]

    hands: List[Hand] = []
    for line in data:
        cards, bid = line.split()
        hands.append(
            Hand(
                cards=cards,
                bid=int(bid)
            )
        )

    return hands


def part1(hands: List[Hand]) -> int:
    for hand in hands:
        hand.strength = [strength_card_part1[card] for card in hand.cards]
        hand.hand_type = hand_types[element_counter(hand.cards)],
    hands.sort(key=lambda x: (x.hand_type, x.strength), reverse=False)

    return sum(hands[i].bid * (i + 1) for i in range(len(hands)))


def part2(hands: List[Hand]) -> int:
    for hand in hands:
        hand.strength = [strength_card_part2[card] for card in hand.cards]
        hand.hand_type = hand_types[element_counter_with_joker(hand.cards)]
    hands.sort(key=lambda x: (x.hand_type, x.strength), reverse=False)

    return sum(hands[i].bid * (i + 1) for i in range(len(hands)))


if __name__ == '__main__':
    input_path = 'input.txt'
    input_data = parse_file(input_path)
    print('part1')
    print(part1(input_data))
    print('part2')
    print(part2(input_data))
