# https://adventofcode.com/2023/day/16
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
    for row in data.split("\n"):
        cards.append(list(row))

    return cards


def go(grid, visited, row, col, dir):
    dr, dc = dir
    new_row, new_col = row + dr, col + dc
    if (
        0 <= new_row < len(grid)
        and 0 <= new_col < len(grid[0])
        and dir not in visited[new_row][new_col]
    ):
        dfs(grid, visited, new_row, new_col, dir)


def dfs(grid, visited, row, col, dir):
    visited[row][col].append(dir)

    if grid[row][col] == "|":
        if dir in [(0, 1), (0, -1)]:
            go(grid, visited, row, col, (1, 0))
            go(grid, visited, row, col, (-1, 0))
        else:
            go(grid, visited, row, col, dir)
    elif grid[row][col] == "-":
        if dir in [(1, 0), (-1, -0)]:
            go(grid, visited, row, col, (0, 1))
            go(grid, visited, row, col, (0, -1))
        else:
            go(grid, visited, row, col, dir)
    elif grid[row][col] == "/":
        if dir == (-1, 0):
            dr, dc = (0, 1)
        if dir == (1, 0):
            dr, dc = (0, -1)
        if dir == (0, 1):
            dr, dc = (-1, 0)
        if dir == (0, -1):
            dr, dc = (1, 0)

        go(grid, visited, row, col, (dr, dc))
    elif grid[row][col] == "\\":
        if dir == (-1, 0):
            dr, dc = (0, -1)
        if dir == (1, 0):
            dr, dc = (0, 1)
        if dir == (0, 1):
            dr, dc = (1, 0)
        if dir == (0, -1):
            dr, dc = (-1, 0)
        go(grid, visited, row, col, (dr, dc))
    elif grid[row][col] == ".":
        go(grid, visited, row, col, dir)


def part1(file_name: str) -> int:
    grid = read_data(file_name=file_name)
    f = []
    n, m = len(grid), len(grid[0])

    for i in range(m):
        visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dfs(grid, visited, 0, i, (1, 0))
        f.append(sum([1 for sub in visited for s in sub if len(s) > 0]))

    for i in range(m):
        visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dfs(grid, visited, n - 1, i, (-1, 0))
        f.append(sum([1 for sub in visited for s in sub if len(s) > 0]))

    for i in range(n):
        visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dfs(grid, visited, i, 0, (0, 1))
        f.append(sum([1 for sub in visited for s in sub if len(s) > 0]))

    for i in range(n):
        visited = [[[] for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dfs(grid, visited, i, m - 1, (0, -1))
        f.append(sum([1 for sub in visited for s in sub if len(s) > 0]))

    print(max(f))


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
