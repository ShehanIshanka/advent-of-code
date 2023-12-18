# https://adventofcode.com/2023/day/15
from typing import Dict, List, Set


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = data.split(",")

    return cards


def hash(string):
    cur_val = 0
    for i in string:
        cur_val = (cur_val + ord(i)) * 17 % 256

    return cur_val


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)

    boxes = {}
    for i in data:
        if "=" in i:
            label, val = i.split("=")
            s = True
            t = boxes.get(hash(label), [])
            for p, q in enumerate(t):
                if q[0] == label:
                    s = False
                    t[p] = (label, int(val))

            if s:
                t.append((label, int(val)))

            boxes[hash(label)] = t
        elif "-" in i:
            label, val = i.split("-")
            t = boxes.get(hash(label), [])
            t1 = []
            for p, q in enumerate(t):
                if q[0] != label:
                    t1.append(q)

            boxes[hash(label)] = t1

    f = 0
    for i, j in boxes.items():
        for a, b in enumerate(j):
            f = f + (i + 1) * (a + 1) * b[1]

    print(f)


def part2(file_name: str) -> int:
    data = read_data(file_name)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
