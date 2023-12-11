# https://adventofcode.com/2023/day/11
from typing import Dict, List, Set


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

    cards = []
    for row in data.split("\n"):
        cards.append(list(map(lambda x: 0 if x == "." else 1, list(row))))

    rows, cols = [], []
    i = 0
    c = len(cards)
    while i < c:
        if sum(cards[i]) == 0:
            rows.append(i)
        i = i + 1

    i = 0
    d = len(cards[0])
    while i < d:
        s = sum([k[i] for k in cards])
        if s == 0:
            cols.append(i)
        i = i + 1

    v = [
        (i, j)
        for i in range(len(cards))
        for j in range(len(cards[i]))
        if cards[i][j] == 1
    ]

    return cards, v, rows, cols


def part1(file_name: str) -> int:
    data, v, rows, cols = read_data(file_name=file_name)
    times = 1000000
    s = 0
    for x in v:
        for y in v:
            a, b = 0, 0
            m1, m2 = min(x[0], y[0]), max(x[0], y[0])
            for p in rows:
                if m1 < p < m2:
                    a = a + 1
            m3, m4 = min(x[1], y[1]), max(x[1], y[1])
            for p in cols:
                if m3 < p < m4:
                    b = b + 1

            s = s + (m2 - m1 - a) + (m4 - m3 - b) + (a + b) * times
    print(s / 2)


def part2(file_name: str) -> int:
    data = read_data(file_name)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
