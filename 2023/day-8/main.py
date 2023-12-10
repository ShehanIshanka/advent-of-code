# https://adventofcode.com/2023/day/7
from typing import Dict, List, Set

order = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

# 32T3K 765
INS = {"L": 0, "R": 1}


def read_data(file_name: str) -> Dict[str, int]:
    with open(file_name, "r") as file:
        data = file.read()

    splits = data.split("\n")
    instructions = list(splits[0])

    f = {}
    for row in splits[2:]:
        i, j = row.split(" = ")
        a, b = j.replace("(", "").replace(")", "").replace(",", "").split()
        f[i] = [a, b]
    return instructions, f


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
    inst, data = read_data(file_name=file_name)

    steps = 0
    val = "AAA"
    while val != "ZZZ":
        for i in inst:
            val = data[val][INS[i]]
            steps += 1
            if val == "ZZZ":
                break

    return steps


def part3(file_name: str) -> int:
    print("------")
    inst, data = read_data(file_name=file_name)

    nodes = [i for i in data.keys() if i[-1] == "A"]
    s = []
    for val in nodes:
        steps = 0

        while val[-1] != "Z":
            for i in inst:
                val = data[val][INS[i]]
                steps += 1
                if val[-1] == "Z":
                    break

        s.append(steps)

    print(s)
    return steps  # 9177460370549


def part2(file_name: str) -> int:
    inst, data = read_data(file_name=file_name)

    nodes = [i for i in data.keys() if i[-1] == "A"]
    print(nodes)
    steps = 0
    l = len(nodes)
    s = True
    while s:
        for i in inst:
            f = 0
            for n, val in enumerate(nodes):
                x = data[val][INS[i]]
                nodes[n] = x

                if x[-1] == "Z":
                    f = f + 1
            steps += 1
            if f == l:
                s = False
                break

    return steps


if __name__ == "__main__":
    # print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 5905
    # print(part2(file_name="test1.txt"))  # 5905
    # print(part2(file_name="input.txt"))  # 254083736

    print(part3(file_name="test.txt"))  # 5905
    print(part3(file_name="test1.txt"))  # 5905
    print(part3(file_name="input.txt"))  # 254083736
