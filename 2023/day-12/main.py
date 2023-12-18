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

    cards, coms = [], []
    for row in data.split("\n"):
        a, b = row.split()
        cards.append(a)
        coms.append(list(map(int, b.split(","))))

    return cards, coms


from itertools import product


def get_all_combinations(symbols, length):
    return ["".join(i) for i in list(product(symbols, repeat=length))]


def part1(file_name: str) -> int:
    data, com = read_data(file_name=file_name)
    c = 0
    for i in range(len(data)):
        p = ".".join(["#" * j for j in com[i]])
        t = re.sub(r"\.{2,}", ".", data[i])

        if t[0] == ".":
            p = "." + p
        if t[-1] == ".":
            p = p + "."

        # print(p, t)
        # # print(len(p), len(t))
        #
        # p1 = [s for s in p.split(".") if s]
        # t1 = [s for s in t.split(".") if s]
        #
        # print(p1, t1)

        n, m = len(p), len(t)

        b = [q for q in range(m) if t[q] == "?"]
        y = []
        for u in get_all_combinations(["#", "."], len(b)):
            replaced_string = t.replace("?", "{}")
            r = re.sub(r"\.{2,}", ".", replaced_string.format(*u))
            # print(com[i], r, [z.count("#") for z in r.split(".") if "#" in z])
            # y.l()
            if com[i] == [z.count("#") for z in r.split(".") if "#" in z]:
                y.append(u)

        # print(p, t, len(set(y)), set(y))
        c = c + len(set(y))

    print(c)


def part2(file_name: str) -> int:
    data = read_data(file_name)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
