# https://adventofcode.com/2023/day/17
from typing import Dict, List, Set
import sys

sys.setrecursionlimit(100000000)


def print_grid(grid):
    for x in grid:
        print("".join(map(str, x)))
        # print("".join(map(lambda x: "#" if len(x) > 0 else "O", x)))


def is_valid_cell(grid, visited, row, col):
    rows, cols = len(grid), len(grid[0])
    return (
        0 <= row < rows
        and 0 <= col < cols
        and not visited[row][col]
        and grid[row][col] != -1
    )


def is_valid_path(path):
    if len(path) < 3:
        return True
    h = []
    node = path[-1]
    for a in path[-4:-1][::-1]:
        if abs(a[0] - node[0]) == 0 and abs(a[1] - node[1]) == 1:
            h.append("ROW")
        elif abs(a[0] - node[0]) == 1 and abs(a[1] - node[1]) == 0:
            h.append("COL")
        else:
            h.append("TURN")
        node = a
    # print(h, set(h), path)
    if len(h) > 2 and len(set(h)) == 1 and h[-1] in ["COL", "ROW"]:
        # print("aaaaa",path)
        return False

    return True


def dfs_paths(grid, start, end, path, paths, visited):
    print(start)
    # print(start)
    rows, cols = len(grid), len(grid[0])
    row, col = start

    path.append(start)
    if not is_valid_path(path):
        path.pop()
        return
    visited[row][col] = True

    if start == end:
        paths.append(list(path))
        v = 0
        for i, j in path:
            v = v + grid[i][j]
        print(v)
    else:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_cell(grid, visited, new_row, new_col):
                dfs_paths(grid, (new_row, new_col), end, path, paths, visited)

    path.pop()
    visited[row][col] = False


def find_all_paths(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    paths = []
    dfs_paths(grid, start, end, [], paths, visited)
    return paths


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = []
    for row in data.split("\n"):
        # cards.append(list(map(int,list(row)))[0:5])
        cards.append(list(map(int, list(row))))

    return cards


def part1(file_name: str) -> int:
    # grid = read_data(file_name=file_name)[:2]
    grid = read_data(file_name=file_name)
    n, m = len(grid), len(grid[0])
    start_node = (0, 0)  # Replace with your start node coordinates
    end_node = (n - 1, m - 1)
    all_paths = find_all_paths(grid, start_node, end_node)
    p = []
    for a in all_paths:
        print(a)
        v = 0
        for i, j in a:
            v = v + grid[i][j]

        p.append(v)

    print(p)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
