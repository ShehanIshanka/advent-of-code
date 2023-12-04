# https://adventofcode.com/2023/day/4
from typing import Dict, List, Set


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = {}
    for row in data.split("\n"):
        card, number_lists = row.split(":")
        card_id = card.split()[1].strip()

        w, n = number_lists.split(" | ")
        winning_numbers = filter(None, w.strip().split(" "))
        my_numbers = filter(None, n.strip().split(" "))
        cards[card_id] = [set(map(int, winning_numbers)), set(map(int, my_numbers))]

    return cards


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)

    points = 0
    for _, d in data.items():
        winning_numbers, my_numbers = d
        winning_number_count = len(winning_numbers.intersection(my_numbers))
        w = winning_number_count - 1
        points = points + ((2**w) if w > -1 else 0)

    return points


def part2(file_name: str) -> int:
    data = read_data(file_name)

    scratch_cards = [1] * len(data)
    pos = 0

    for _, d in data.items():
        winning_numbers, my_numbers = d
        winning_number_count = len(winning_numbers.intersection(my_numbers))
        scratch_cards[pos + 1 : pos + winning_number_count + 1] = [  # noqa: E203
            c + scratch_cards[pos]
            for c in scratch_cards[
                pos + 1 : pos + winning_number_count + 1  # noqa: E203
            ]
        ]
        pos = pos + 1

    return sum(scratch_cards)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    print(part2(file_name="test.txt"))  # 30
    print(part2(file_name="input.txt"))  # 5833065
