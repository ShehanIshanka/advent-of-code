# https://adventofcode.com/2023/day/9
from typing import Dict, List, Set


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = []
    for row in data.split("\n"):
        cards.append(list(map(int, row.split())))

    return cards


def extrapolate(seq):
    if seq.count(0) == len(seq):
        return 0
    diff = [j - i for i, j in zip(seq[:-1], seq[1:])]
    return seq[-1] + extrapolate(diff)


def extrapolate_back(seq):
    if seq.count(0) == len(seq):
        return 0
    diff = [j - i for i, j in zip(seq[:-1], seq[1:])]
    return seq[0] - extrapolate_back(diff)


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)
    s = [extrapolate(n) for n in data]
    print(sum(s))


def part2(file_name: str) -> int:
    data = read_data(file_name=file_name)
    s = [extrapolate_back(n) for n in data]
    print(s)
    print(sum(s))


if __name__ == "__main__":
    # print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    # 2075724809

    print(part2(file_name="test.txt"))  # 30
    print(part2(file_name="input.txt"))  # 5833065
