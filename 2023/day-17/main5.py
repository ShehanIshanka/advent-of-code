# https://adventofcode.com/2023/day/17
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
        cards.append(list(map(lambda x: int(x), list(row))))

    return cards


import heapq


def grid_to_graph(grid):
    graph = {}
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in graph:
                graph[(r, c)] = {}

            # Add edges for adjacent cells (up, down, left, right)
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    graph[(r, c)][(new_row, new_col)] = grid[new_row][new_col]

    return graph


def is_valid_nav(turns, predecessors, current_node, nav):
    node = current_node
    h = [nav]
    while node is not None:
        if node is None:
            return True

        h = [turns[node]] + h

        # if current_node == (2, 4):

        if len(h) > 3:
            print(h, current_node, len(set(h)) == 1 and h[-1] in ["COL", "ROW"])
            if len(set(h)) == 1 and h[-1] in ["COL", "ROW"]:
                # print("breaking", current_node)
                return False
            else:
                return True

        node = predecessors[current_node]

    return True


def get_navigation(previous_nav, prev, cur):
    if abs(prev[0] - cur[0]) == 0 and abs(prev[1] - cur[1]) == 1:
        val = "ROW"
    elif abs(prev[0] - cur[0]) == 1 and abs(prev[1] - cur[1]) == 0:
        val = "COL"

    return val


def dijkstra(grid, start, end=None, pr=None):
    graph = grid_to_graph(grid)
    pq = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    turns = {node: None for node in graph}

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        # print(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():

            new_dist = current_dist + weight

            if new_dist < distances[neighbor]:
                nav = get_navigation(turns[current_node], current_node, neighbor)
                print("nav is ", current_node, neighbor, nav)
                if current_node == (2, 3):
                    print(
                        "----",
                        neighbor,
                        is_valid_nav(turns, predecessors, current_node, nav),
                    )

                if is_valid_nav(turns, predecessors, current_node, nav):
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = current_node
                    turns[neighbor] = nav
                    heapq.heappush(pq, (new_dist, neighbor))

    return distances, predecessors


def get_path(predecessors, end):
    # Reconstruct path from start to end
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()  # Reverse to get the correct order from start to end

    return path


def part1(file_name: str) -> int:
    grid = [
        [1, 12, 13, 12, 1],
        [11, 2, 13, 12, 1],
        [1, 11, 13, 12, 1],
        [1, 1, 13, 12, 1],
    ]
    # grid = read_data(file_name=file_name)

    n, m = len(grid) - 1, len(grid[0]) - 1
    start_node = (0, 0)
    end_node = (n, m)
    # end_node = (12, 11)

    result, pred = dijkstra(grid, start_node, end_node)
    print(result[end_node] + grid[0][0])
    print(get_path(pred, end_node))
    print(result)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
