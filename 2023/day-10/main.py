# https://adventofcode.com/2023/day/10
from typing import Dict, List, Set

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
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] != "." and visited[x][y] == -1


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


# def dfs_util(x, y, grid, visited, pre):
#     # print(x,y, grid[x][y])
#     if grid[x][y] == "S":
#         visited[x][y] = 0
#     elif grid[x][y] in turn.keys():
#         visited[x][y] = pre + 1
#
#     # print(turn.get(grid[x][y], directions))
#     directions = turn.get(grid[x][y], all_directions)
#     for dx, dy in directions:
#         new_x, new_y = x + dx, y + dy
#         # print(
#         #     (x, y),
#         #     grid[x][y],
#         #     (new_x, new_y),
#         #     visited[new_x][new_y],
#         #     grid[new_x][new_y],
#         #     is_valid(new_x, new_y, grid, visited),
#         #     get_dir(grid[x][y], grid[new_x][new_y]),
#         # )
#         if is_valid(new_x, new_y, grid, visited) and get_dir(
#             grid[x][y], grid[new_x][new_y]
#         ):
#             dfs_util(new_x, new_y, grid, visited, visited[x][y])


def conver(x):
    return "*" if x == -1 else "|" + str(x) + "|"


def print_grid(grid, visited):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        d = ""
        for j in range(cols):
            d += "." if visited[i][j] == -1 else str(visited[i][j])
        print(d)


from collections import deque


def bfs_on_grid_from_index(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    visited = [[-1 for _ in range(cols)] for _ in range(rows)]

    queue = deque([(start_x, start_y)])  # Initialize queue with starting index
    visited[start_x][start_y] = True
    pre = 0

    while queue:
        x, y = queue.popleft()
        if grid[x][y] == "S":
            visited[x][y] = 0
        elif grid[x][y] in turn.keys():
            pre = visited[x][y]

        directions = turn.get(grid[x][y], all_directions)
        for dx, dy in directions:  # Check neighbors
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, grid, visited) and get_dir(
                grid[x][y], grid[new_x][new_y]
            ):
                visited[new_x][new_y] = pre + 1
                queue.append((new_x, new_y))

    print_grid(grid, visited)
    return max([item for sublist in visited for item in sublist])


def part1(file_name: str) -> int:
    start, data = read_data(file_name=file_name)
    x = bfs_on_grid_from_index(data, start[0], start[1])
    print(x)
    print("---------")


def part2(file_name: str) -> int:
    data = read_data(file_name=file_name)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    print(part1(file_name="test2.txt"))  # 13
    print(part1(file_name="test3.txt"))  # 13
    print(part1(file_name="input.txt"))  # 20667

    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
