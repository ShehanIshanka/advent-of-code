# https://adventofcode.com/2023/day/14
from typing import Dict, List, Set


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = []
    for row in data.split("\n"):
        cards.append(row)

    return cards


def print_grid(grid):
    for i in grid:
        print(i)


def tilt(data, l):

    p = []
    f = 0
    for i in data:
        d = list(i)
        x = []
        for j in range(len(i)):
            if d[j] == ".":
                x.append(j)
                continue
            if d[j] == "#":
                x = []
                continue
            if len(x) > 0 and d[j] == "O":
                h = x[0]
                x.remove(h)
                d[h] = "O"
                d[j] = "."
                x.append(j)

        # for c in range(len(d)):
        #     if d[c] == "O":
        #         f = f + l - c

        p.append("".join(d))

    return p, f


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)
    l = len(data)
    dir = {
        0: "N",
        1: "W",
        2: "S",
        3: "E",
    }
    m = []

    for v in range(200):
        for i in range(4):
            if dir[i] == "N":
                data = ["".join(row) for row in zip(*data)]
                l = len(data)
                data, f = tilt(data, l)
                data = ["".join(row) for row in zip(*data)]
            if dir[i] == "W":
                l = len(data)
                data, f = tilt(data, l)
            if dir[i] == "S":
                data = ["".join(row) for row in zip(*data[::-1])]
                l = len(data)
                data, f = tilt(data, l)
                data = data[::-1]
                data = ["".join(row[::-1]) for row in zip(*data)][::-1]
            if dir[i] == "E":
                data = ["".join(row[::-1]) for row in data]
                l = len(data)
                data, f = tilt(data, l)
                data = ["".join(row[::-1]) for row in data]

        f = 0
        for c in range(len(data)):
            for j in data[c]:
                if j == "O":
                    f = f + l - c
        print(v + 1, f)

        # if data in m:
        #     print(m.index(data))
        #     break
        m.append(data)
        # print(data)
        # print(v)
        # print_grid(data)
        # print("-"*100)


def part2(file_name: str) -> int:
    data = read_data(file_name)


if __name__ == "__main__":
    # print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667
