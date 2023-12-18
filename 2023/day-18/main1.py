# https://adventofcode.com/2023/day/18
from typing import Dict, List, Set
import sys

sys.setrecursionlimit(100000)


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

        h = traverse(grid, n, j, dir, k)
        f.extend(h)
        n = h[-1]

        # print(n)
        # break
    return f


def is_in(x, y, visited):
    def is_valid1(x, y, grid1, visited1):
        rows, cols = len(grid1), len(grid1[0])
        return (
            0 <= x < rows and 0 <= y < cols and grid1[x][y] < 0 and visited1[x][y] == -1
        )

    def dfs_util1(x, y, grid1, visited1):
        rows, cols = len(grid1), len(grid1[0])
        visited1[x][y] = 1
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]  # Possible directions: down, up, right, left

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid1(new_x, new_y, grid1, visited1):
                if new_x == 0 or new_x == rows - 1 or new_y == 0 or new_y == cols - 1:
                    return True
                t = dfs_util1(new_x, new_y, grid1, visited1)
                if t:
                    return True
        return False

    def dfs_on_grid1(x, y, grid1):
        rows, cols = len(grid1), len(grid1[0])
        visited1 = [[-1 for _ in range(cols)] for _ in range(rows)]

        return dfs_util1(x, y, grid1, visited1)

        # print_grid(grid1, visited1)

    return 0 if dfs_on_grid1(x, y, visited) else 1



def part1(file_name: str) -> int:
    data, l, d = read_data(file_name=file_name)
    print(l, d)
    grid = [["."] * l*4 for i in range(d*4)]
    start = (l, d)
    print(start)
    grid[start[0]][start[1]] = 1
    f = dig(grid, data, start)

    ma_x, ma_y = 0, 0
    min_x, min_y = float("inf"), float("inf")
    for i, j in f:
        ma_x = max(ma_x, i)
        ma_y = max(ma_y, j)

        min_x = min(min_x, i)
        min_y = min(min_y, j)


    v = []
    for i, j in f:
        a,b = i - min_x, j -min_y
        if (a,b) not in v:
            v.append((a,b))

    grid1 = [[float("-inf")] * (ma_y-min_y + 2) for i in range(ma_x -min_x + 2)]
    # grid1 = [["."] * (ma_y-min_y + 1) for i in range(ma_x -min_x + 1)]
    y =1
    for i, j in v:
        grid1[i][j] = y
        y = y + 1

    # print_grid(grid1)
    visited = grid1

    ma = max([item for sublist in visited for item in sublist])

    rows, cols = len(visited), len(visited[0])
    i, j = 0, 0
    while i < cols:
        j = 1
        while j < rows:
            if (
                    visited[j - 1][i] < 0
                    or visited[j][i] < 0
                    or abs(visited[j][i] - visited[j - 1][i]) == 1
                    or abs(visited[j - 1][i] - visited[j][i]) == ma - 1
            ):
                # print(j)
                j = j + 1
                continue
            # print(j,cols)
            visited.insert(j, [-111111111111111111111111] * len(visited[j]))

            for v in range(len(visited[j])):
                if abs(visited[j - 1][v] - visited[j + 1][v]) == ma - 1:
                    visited[j][v] = ma + 1
                    ma = ma + 1
                elif abs(visited[j - 1][v] - visited[j + 1][v]) == 1:
                    k = min(visited[j - 1][v], visited[j + 1][v])
                    if k == visited[j - 1][v]:
                        u = j - 1
                    else:
                        u = j + 1
                    k = k + 1
                    for c in range(len(visited)):
                        for d in range(len(visited[c])):
                            if c == u and d == v:
                                continue
                            if visited[c][d] >= k:
                                visited[c][d] += 1
                            ma = max(visited[c][d], ma)
                    visited[j][v] = k
                    ma = max(k, ma)
            j = j + 2
            rows = rows + 1
        i = i + 1

    kl1 = []
    de = set()
    print("done")

    ma = max([item for sublist in visited for item in sublist])
    rows, cols = len(visited), len(visited[0])
    i, j = 0, 0
    while i < rows:
        j = 1
        while j < cols:
            if (
                    visited[i][j - 1] < 0
                    or visited[i][j] < 0
                    or abs(visited[i][j] - visited[i][j - 1]) == 1
                    or abs(visited[i][j] - visited[i][j - 1]) == ma - 1
            ):
                # print(j)
                j = j + 1
                continue
            # print(j,cols)

            for n in range(len(visited)):
                u = j
                if abs(visited[n][j] - visited[n][j - 1]) == ma - 1:
                    k = ma + 1
                    visited[n].insert(j, k)
                    u = j + 1
                    # for c in range(len(visited)):
                    #     for d in range(len(visited[c])):
                    #         if visited[c][d] >= k or (c != n and d != j):
                    #             visited[c][d] += 1
                    ma += 1

                elif abs(visited[n][j] - visited[n][j - 1]) == 1:
                    k = min(visited[n][j - 1], visited[n][j])
                    if k == visited[n][j - 1]:
                        u = j - 1
                    else:
                        u = j

                    for c in range(len(visited)):
                        for d in range(len(visited[c])):
                            if c == n and d == u:
                                continue
                            if visited[c][d] >= k:
                                visited[c][d] += 1
                            ma = max(visited[c][d], ma)
                    visited[n].insert(j, k + 1)
                    ma = max(k + 1, ma)
                    # ma = max([item for sublist in visited for item in sublist])
                    # for c in range(j+1, len(visited[n])):
                    #     visited[n][c] += 1
                else:
                    visited[n].insert(j, -11111111111111111111111)
                    u = j + 1
            # print_grid(grid, visited)
            # print(i,j)
            # j.a()
            j = j + 2
            cols = cols + 1
        i = i + 1

    print("done")
    kl2 = []

    #
    d = 0
    for i in range(rows):
        for j in range(cols):
            # print(i,j)
            d += 1 if visited[i][j] == float("-inf") and is_in(i, j, visited) else 0
    print(d)
    print(len(de), len(kl1), len(kl2))
    print(ma)
    print(ma+d)

    # print_grid(grid1)






if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print("*"*1000)
    print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
