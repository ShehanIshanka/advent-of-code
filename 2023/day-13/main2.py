# https://adventofcode.com/2023/day/13
from typing import Dict, List, Set


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards, pattern = [], []
    for row in data.split("\n"):
        if row == "":
            cards.append(pattern)
            pattern = []
            continue
        pattern.append(row)
    cards.append(pattern)
    return cards


def smudge(str1, str2):

    return sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)


def get_matches(patterns):
    h1, h2, l = [], [], len(patterns)
    # p = [int(l / 2)] if l % 2 == 0 else [int(l / 2) , int(l / 2)]
    # g = [int(l / 2)] if l % 2 == 0 else [int(l / 2) , int(l / 2) + 1]

    for x in range(1, l):
        c = 0
        for t in range(1, x + 1):
            if x - t == x + t - 1:
                continue
            if x + t - 1 > l - 1:
                c = c + 1 if c > 0 else c
                break
            if x - t < 0:
                break
            if patterns[x - t] == patterns[x + t - 1]:
                # print(x -t, x + t - 1,c, x, patterns[x - t], patterns[x + t - 1])
                c = c + 1
            else:
                c = 0
                break

        if c == x:
            h1.append(x)
        if c == l - x + 1:
            h2.append(x)

    # print(h1,h2)
    if len(h1) > 0:
        return max(h1)
    if len(h2) > 0:
        return max(h2) if max(h2) != l else 0

    return 0


def get_matches_line(patterns, f):
    h1, h2, l = [], [], len(patterns)
    p = 0

    for x in range(1, l):
        c = 0
        for t in range(1, x + 1):
            print(x, patterns[x - t], patterns[x + t - 1])

            if x - t == x + t - 1:
                continue
            if x + t - 1 > l - 1:
                c = c + 1 if c > 0 else c
                break
            if x - t < 0:
                c = c + 1 if c > 0 else c
                break
            if patterns[x - t] == patterns[x + t - 1]:
                # print(x -t, x + t - 1,c, x, patterns[x - t], patterns[x + t - 1])
                c = c + 1
            elif smudge(patterns[x - t], patterns[x + t - 1]) == 1:
                print(x, 9)
                p = p + 1
                c = c + 1

            if c > 0:
                break

        # print(x)
        if f == x:
            continue
        if p == 1:
            return x
    #     if c == l - x + 1 and p == 1:
    #         h2.append(x)
    #
    # # print(h1,h2)
    # if len(h1) > 0 and f !=  max(h1):
    #     return max(h1)
    # if len(h2) > 0 and f !=  max(h2):
    #     return max(h2) if max(h2) != l else 0

    return 0


def part1(file_name: str) -> int:
    data = read_data(file_name=file_name)
    s = 0
    a, b = [], []
    for i, patterns in enumerate(data):
        h = get_matches(patterns)

        transposed_matrix = ["".join(row) for row in zip(*patterns)]

        v = get_matches(transposed_matrix)

        print(h, v)

        if h != 0:
            a.append("h")
            b.append(h)
            s = s + h * 100
            continue

        a.append("v")
        b.append(v)
        s = s + v

        print("==========")

    s = 0
    for patterns in data:
        h = get_matches(patterns)

        transposed_matrix = ["".join(row) for row in zip(*patterns)]

        v = get_matches_line(transposed_matrix, b[i])

        print(h, v)

        if h != 0:
            s = s + h * 100
            continue

        s = s + v

        print("==========")

    print(s)


def part2(file_name: str) -> int:
    data = read_data(file_name)


if __name__ == "__main__":
    print(part1(file_name="tes1t.txt"))  # 13
    print("*" * 100)
    # print(part1(file_name="test.txt"))  # 13
    print("*" * 100)
    # print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
