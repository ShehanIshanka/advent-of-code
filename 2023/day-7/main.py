# https://adventofcode.com/2023/day/7
from typing import Dict, List, Set

order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

# 32T3K 765


def read_data(file_name: str) -> Dict[str, int]:
    with open(file_name, "r") as file:
        data = file.read()

    hands = {}
    for row in data.split("\n"):
        hand, bid = row.split()
        hands[hand] = int(bid)

    return hands


# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card

from collections import Counter
from functools import cmp_to_key
import re


def replace_J_highest_label(text):
    highest_label = max(re.findall("[A-I]", text))
    replaced_text = re.sub("J", highest_label, text)
    return replaced_text


def get_hand_type(hand: str):
    if "J" in hand:
        sorted_counter = sorted(
            Counter(hand).items(), key=lambda item: item[1], reverse=True
        )
        c = None
        for x in sorted_counter:
            if x[0] != "J":
                c = x[0]
                break

        if c is not None:
            hand = hand.replace(c, "J")

    sorted_counter = sorted(
        Counter(hand).items(), key=lambda item: item[1], reverse=True
    )

    if sorted_counter[0][1] == 5:
        return 6

    if sorted_counter[0][1] == 4:
        return 5

    if sorted_counter[0][1] == 3 and sorted_counter[1][1] == 2:
        return 4

    if sorted_counter[0][1] == 3:
        return 3

    if sorted_counter[0][1] == 2 and sorted_counter[1][1] == 2:
        return 2

    if sorted_counter[0][1] == 2:
        return 1

    return 0


def comp(hand1, hand2):
    h1 = get_hand_type(hand1)
    h2 = get_hand_type(hand2)

    if h1 < h2:
        return -1
    elif h1 > h2:
        return 1
    else:
        for i, (a, b) in enumerate(zip(hand1, hand2)):
            if order.index(a) == order.index(b):
                continue
            if order.index(a) < order.index(b):
                return -1
            if order.index(a) > order.index(b):
                return 1

        return 0


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)
    p = sorted(list(data.keys()), key=cmp_to_key(comp))
    print(p)
    s = 0
    for i, j in enumerate(p):
        s = s + data[j] * (i + 1)
    # points = 0
    # for _, bid in data.items():
    #     winning_numbers, my_numbers = d
    #     winning_number_count = len(winning_numbers.intersection(my_numbers))
    #     w = winning_number_count - 1
    #     points = points + ((2**w) if w > -1 else 0)
    #
    # return points
    print(s)


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

    # print(part2(file_name="test.txt"))  # 5905
    # print(part2(file_name="input.txt"))  # 254083736
