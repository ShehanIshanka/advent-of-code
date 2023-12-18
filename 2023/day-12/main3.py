# https://adventofcode.com/2023/day/12
from typing import Dict, List, Set
import re


def print_grid(visited):
    rows, cols = len(visited), len(visited[0])
    for i in range(rows):
        d = ""
        for j in range(cols):
            d += str(visited[i][j])
        print(d)


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards, coms, counts = [], [], []
    for row in data.split("\n"):
        a, b = row.split()
        a = "?".join([a] * 1)
        b = ",".join([b] * 1)
        counts.append(a.count("?"))
        cards.append(a.replace("?", "{}"))
        coms.append(b)

    return cards, coms, counts


from itertools import product, combinations_with_replacement, permutations

combs = {}


def get_all_combinations(symbols, length):
    combs[length] = combs.get(
        length, ["".join(i) for i in list(product(symbols, repeat=length))]
    )
    return combs[length]


def part1(file_name: str):
    data, coms, counts = read_data(file_name=file_name)

    c = 0
    for i in range(len(data)):
        w = ["#" * int(j) for j in coms[i].split(",")]

        t = data[i]
        b = t.count("#") - counts[i]
        y = 0

        for u in get_all_combinations(["#", "."], b):
            r = re.sub(r"\.{2,}", ".", t.format(*u))
            if coms[i] == ",".join(
                [str(z.count("#")) for z in r.split(".") if "#" in z]
            ):
                y = y + 1

        c = c + y

    print(c)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 525152
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
