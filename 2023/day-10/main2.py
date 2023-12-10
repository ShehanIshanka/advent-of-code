# https://adventofcode.com/2023/day/10
from typing import Dict, List, Set
import sys

sys.setrecursionlimit(100000000)
# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

turn = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(0, 1), (-1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}

all_directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
]


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = []
    i = 0
    for row in data.split("\n"):
        if "S" in row:
            start = (i, row.index("S"))
        cards.append(list(row))
        i = i + 1

    return start, cards


def is_valid(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != "."


turns = {
    "|": ["|", "7", "J", "F", "L"],
    "-": ["-", "7", "J", "F", "L"],
    "L": ["-", "|", "J", "7", "F"],
    "J": ["-", "|", "L", "F", "7"],
    "7": ["-", "|", "L", "J", "F"],
    "F": ["-", "|", "7", "J", "L"],
}


def get_dir(cur, next):
    if cur == "S":
        return True

    if next in turns.get(cur, []):
        return True

    return False


def dfs_util(x, y, grid, visited, rec, pre):
    # print(x,y, grid[x][y])
    if grid[x][y] == "S":
        visited[x][y] = 1
    elif grid[x][y] in turn.keys():
        visited[x][y] = pre + 1
    rec[x][y] = True

    # print(turn.get(grid[x][y], directions))
    directions = turn.get(grid[x][y], all_directions)
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        # print(
        #     (x, y),
        #     grid[x][y],
        #     (new_x, new_y),
        #     grid[new_x][new_y],
        #     visited[new_x][new_y],
        #     rec[new_x][new_y],
        #     is_valid(new_x, new_y, grid, visited),
        #     get_dir(grid[x][y], grid[new_x][new_y]),
        # )
        if (
            is_valid(new_x, new_y, grid, visited)
            and get_dir(grid[x][y], grid[new_x][new_y])
            and visited[new_x][new_y] == float("-inf")
        ):
            if dfs_util(new_x, new_y, grid, visited, rec, visited[x][y]):
                return True
        elif (
            is_valid(new_x, new_y, grid, visited)
            and get_dir(grid[x][y], grid[new_x][new_y])
            and rec[new_x][new_y]
        ):
            continue

    rec[x][y] = False
    return False


def print_grid(grid, visited):
    rows, cols = len(visited), len(visited[0])
    for i in range(rows):
        d = ""
        for j in range(cols):
            # d += "I" if visited[i][j] == float("-inf") else "1" if visited[i][j] < 0 else "."
            # d += "1" if visited[i][j] < 0 else "."
            # d += "." if visited[i][j] < 0 else str(1)
            d += "..." if visited[i][j] < 0 else str(visited[i][j] + 100)
            # d +=  str(visited[i][j])
        print(d)


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


def dfs_on_grid_from_index(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    visited = [[float("-inf") for _ in range(cols)] for _ in range(rows)]
    rec = [[False for _ in range(cols)] for _ in range(rows)]

    dfs_util(start_x, start_y, grid, visited, rec, 0)
    # print_grid(grid, visited)
    # print("-" * 100)

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
                    # ma = max([item for sublist in visited for item in sublist])

            # for n in range(j+1, len(visited)):
            #     for c in range(len(visited[n])):
            #         visited[n][c] += 1
            # print(j)
            # print_grid(grid, visited)
            # j.a()
            j = j + 2
            rows = rows + 1
        i = i + 1

    kl1 = []
    de = set()
    print("done")
    # for i in range(rows):
    #     for j in range(cols):
    #         if visited[i][j] == float("-inf") and is_in(i, j, visited) :
    #             kl1.append(f"{i}:{j}")
    #             de.add(f"{i}:{j}")

    # print_grid(grid, visited)
    # print("-" * 100)
    # visited = vw
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
    # for i in range(rows):
    #     for j in range(cols):
    #         if visited[i][j] == float("-inf") and is_in(i, j, visited) :
    #             kl2.append(f"{i}:{j}")
    #             de.add(f"{i}:{j}")

    # print_grid(grid, visited)
    # print("-" * 100)

    #
    d = 0
    for i in range(rows):
        for j in range(cols):
            d += 1 if visited[i][j] == float("-inf") and is_in(i, j, visited) else 0
    print(d)
    print(len(de), len(kl1), len(kl2))
    return ma
    # # Traverse the entire grid
    # for i in range(rows):
    #     for j in range(cols):
    #         if grid[i][j] == 1 and not visited[i][j]:
    #             dfs_util(i, j, grid, visited)


def part1(file_name: str) -> int:
    start, data = read_data(file_name=file_name)
    x = dfs_on_grid_from_index(data, start[0], start[1])
    print(x)
    print((x + 1) / 2)
    print("---------")


def part2(file_name: str) -> int:
    data = read_data(file_name=file_name)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="test2.txt"))  # 13
    print(part1(file_name="test3.txt"))  # 13
    print(part1(file_name="test4.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
