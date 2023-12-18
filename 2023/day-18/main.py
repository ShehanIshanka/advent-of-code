# https://adventofcode.com/2023/day/18
from typing import Dict, List, Set
import sys

sys.setrecursionlimit(100000000)


def print_grid(grid):
    for x in grid:
        print("".join(map(str, x)))
        # print("".join(map(lambda x: "#" if len(x) > 0 else "O", x)))


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = []
    r, l, u, d = [], [], [], []
    for row in data.split("\n"):
        a, b, c = row.split()
        cards.append([a, int(b), c[1:-1]])
        if a == "R":
            r.append(int(b))
        if a == "L":
            l.append(int(b))
        if a == "U":
            u.append(int(b))
        if a == "D":
            d.append(int(b))

    return cards, max(sum(l), sum(r)), max(sum(u), sum(d))


def traverse(grid, start, length, dir, val):
    n, m = len(grid), len(grid[0])
    node = start
    s = [node]
    for i in range(length):
        node = (node[0] + dir[0], node[1] + dir[1])
        # if 0 <= node[0] < n and 0 <= node[1] < m:
        grid[node[0]][node[1]] = "#"
        s.append(node)

    return s


def dig(grid, data, start):
    n = start
    dir = None
    f = []
    for i, j, k in data:
        if i == "R":
            dir = (0, 1)
        if i == "L":
            dir = (0, -1)
        if i == "D":
            dir = (1, 0)
        if i == "U":
            dir = (-1, 0)
        # if i == "D":
        #     dir = (0, 1)
        # if i == "U":
        #     dir = (0, -1)
        # if i == "L":
        #     dir = (1, 0)
        # if i == "R":
        #     dir = (-1, 0)

        h = traverse(grid, n, j, dir, k)
        f.extend(h)
        n = h[-1]

        # print(n)
        # break
    return f


def shoelace_formula(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return abs(area) / 2.0


# def shoelace_formula(polygonBoundary, absoluteValue=True):
#     nbCoordinates = len(polygonBoundary)
#     nbSegment = nbCoordinates - 1
#
#     l = [
#         (polygonBoundary[i + 1][0] - polygonBoundary[i][0])
#         * (polygonBoundary[i + 1][1] + polygonBoundary[i][1])
#         for i in range(nbSegment)
#     ]
#
#     if absoluteValue:
#         return abs(sum(l) / 2.0)
#     else:
#         return sum(l) / 2.0


def part1(file_name: str) -> int:
    data, l, d = read_data(file_name=file_name)
    print(l, d)
    grid = [["."] * l * 4 for i in range(d * 4)]
    start = (l, d)
    grid[start[0]][start[1]] = 1
    f = dig(grid, data, start)
    f.reverse()
    grid1 = [["."] * l * 4 for i in range(d * 4)]
    v = []
    y = 0
    for i, j in f:
        grid1[i][j] = f" {y} "
        y = y + 1
        if (i, j) not in v:
            v.append((i, j))

    print(f)
    print(v)
    print(shoelace_formula(v))

    print_grid(grid)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
