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
        cards.append(list(map(int, list(row))))

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


def is_valid(predecessors, current_node):
    # print(current_node, predecessors, "*"*100)
    node = current_node
    h = []
    n = {}
    while node is not None:
        if node in n:
            return False
        n[node] = 1
        # print(node, h)
        a = node
        node = predecessors[node]

        if node is None:
            return True

        if abs(a[0] - node[0]) == 0 and abs(a[1] - node[1]) == 1:
            h.append("ROW")
        elif abs(a[0] - node[0]) == 1 and abs(a[1] - node[1]) == 0:
            h.append("COL")
        else:
            h.append("TURN")

        # if current_node == (7,11):
        #     print(h, node)
        if len(h) > 3 and len(set(h[-4:])) == 1 and h[-1] in ["COL", "ROW"]:
            # print("breaking", current_node)
            return False

    return True


def get_available(predecessors, turns, current_node):
    h = []
    node = current_node
    while node is not None:
        if node is None or len(h) == 3:
            break

        node = predecessors[node]
        h.append(turns[node])

    if len(set(h)) == 1:
        return ["COL"] if h[-1] == "ROW" else ["ROW"]


def dijkstra(grid, start, end=None, pr=None):
    graph = grid_to_graph(grid)
    pq = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    if pr is not None:
        predecessors.update(pr)
    turns = {node: None for node in graph}
    missed = {}
    missed_dist = {}

    while pq:
        # print(pq)
        current_dist, current_node = heapq.heappop(pq)
        # print(current_dist, current_node, len(pq))
        # if current_node == (1,5):
        #     print("::::::")
        #     print(current_dist , distances[current_node],pq)

        # if end is not None and current_node == end:
        #     break

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            # if current_node == (1,5):
            # print("------")
            # print(neighbor, current_dist + weight, distances[neighbor], pq, predecessors)

            new_dist = current_dist + weight
            dir = (
                abs(current_node[0] - neighbor[0]),
                abs(current_node[1] - neighbor[1]),
            )

            if new_dist < distances[neighbor]:
                a, b = distances[neighbor], predecessors[neighbor]
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node  # Track predecessors
                if is_valid(predecessors, neighbor):
                    if (
                        abs(current_node[0] - neighbor[0]) == 0
                        and abs(current_node[1] - neighbor[1]) == 1
                    ):
                        v = "ROW"
                    elif (
                        abs(current_node[0] - neighbor[0]) == 1
                        and abs(current_node[1] - neighbor[1]) == 0
                    ):
                        v = "COL"
                    else:
                        v = "TURN"

                    turns[neighbor] = v
                    heapq.heappush(pq, (new_dist, neighbor))
                else:
                    distances[neighbor] = a
                    predecessors[neighbor] = b
                    # print(new_dist, distances[neighbor], current_node, neighbor)
            else:
                b = predecessors[neighbor]
                predecessors[neighbor] = current_node  # Track predecessors

                if is_valid(predecessors, neighbor):
                    missed[neighbor] = current_node
                    missed_dist[neighbor] = new_dist
                predecessors[neighbor] = b
    # Reconstruct path from start to end
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()  # Reverse to get the correct order from start to end

    for i, j in missed:
        pr = {}
        node = (i, j)
        while node is not None:
            if node is None:
                break

            pr[node] = predecessors[node]
            node = predecessors[node]
        # print(pr)
        r, _, p, _ = dijkstra(grid, (i, j), end, pr)
        t = sum([grid[i][j] for i, j in p])

    return distances, predecessors, path, missed


def dijkstra_global(graph):
    all_distances = {}
    for node in graph:
        all_distances[node] = dijkstra(graph, node)
    return all_distances


def part1(file_name: str) -> int:
    grid = read_data(file_name=file_name)
    n, m = len(grid) - 1, len(grid[0]) - 1
    start_node = (0, 0)
    end_node = (n, m)
    # print(g)
    # print(dijkstra_global(grid))
    result, pred, path, missed = dijkstra(grid, start_node, end_node)
    f = [result[end_node]]
    # for i,j in missed:
    #     pr = { }
    #     node = (i,j)
    #     while node is not None:
    #         if node is None:
    #             break
    #
    #         pr[node] = pred[node]
    #         node = pred[node]
    #     # print(pr)
    #     r, _, p, _ = dijkstra(grid, (i,j),end_node, pr)
    #     t = sum([ grid[i][j] for i,j in p])
    #     f.append(t)
    #     print((i,j), t)
    #     print(p)
    print("---" * 20)
    print(f)
    print(min(f))
    print(start_node, end_node, result)
    print(path)
    print(sum([grid[i][j] for i, j in path]))


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
