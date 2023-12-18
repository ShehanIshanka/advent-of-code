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
    while node is not None:
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

        if len(h) > 2 and len(set(h[-3:])) == 1 and h[-1] in ["COL", "ROW"]:
            print("breaking", current_node)
            return False

    return True


def dijkstra(grid, start, end):
    graph = grid_to_graph(grid)
    pq = [(0, start)]
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_node == end:
            break

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                a, b = distances[neighbor], predecessors[neighbor]
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node  # Track predecessors
                if is_valid(predecessors, neighbor):
                    heapq.heappush(pq, (new_dist, neighbor))
                else:

                    distances[neighbor] = a
                    predecessors[neighbor] = b

    # Reconstruct path from start to end
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = predecessors[node]
    path.reverse()  # Reverse to get the correct order from start to end

    return distances[end], path


def bellman_ford_path_between_nodes(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    # Step 1: Initialize distances from the start node to all other nodes as INFINITY
    distances = {(r, c): float("inf") for r in range(rows) for c in range(cols)}
    distances[start] = 0  # Set the distance from start to itself as 0
    predecessors = {node: None for node in distances}

    # Step 2: Relax edges repeatedly until the shortest path to the end node is found
    for _ in range(rows * cols - 1):
        for r in range(rows):
            for c in range(cols):
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if (
                            distances[(r, c)] != float("inf")
                            and grid[new_row][new_col] != -1
                        ):  # Check for obstacles (-1)
                            new_dist = distances[(r, c)] + grid[new_row][new_col]
                            if new_dist < distances[(new_row, new_col)]:
                                bb = (new_row, new_col)
                                a, b = distances[bb], predecessors[bb]
                                distances[bb] = new_dist
                                predecessors[bb] = (r, c)
                                if not is_valid(predecessors, bb):
                                    distances[bb] = a
                                    predecessors[bb] = b
                                elif (new_row, new_col) == end:
                                    # Reconstruct the path
                                    path = []
                                    node = end
                                    while node is not None:
                                        path.append(node)
                                        node = predecessors[node]
                                    path.reverse()
                                    return distances[end], path

    return float("inf"), []  # No path found


INF = float("inf")


def floyd_warshall_path(grid, start, end):
    rows = len(grid)
    cols = len(grid[0])

    # Initialize distances and next nodes for path reconstruction
    dist = [[INF for _ in range(cols)] for _ in range(rows)]
    next_node = [[None for _ in range(cols)] for _ in range(rows)]

    # Set distance to itself as 0 and edges based on the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == -1:
                continue  # Skip obstacles represented as -1
            dist[i][j] = grid[i][j]
            next_node[i][j] = (i, j)

    # Floyd-Warshall algorithm
    for k in range(rows):
        for i in range(rows):
            for j in range(cols):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Reconstruct the path
    path = []
    # while start != end:
    #     if next_node[start[0]][start[1]] is None:
    #         return float('inf'), []  # No path found
    #     path.append(start)
    #     start = next_node[start[0]][start[1]]

    path.append(end)
    return dist[end[0]][end[1]], path


INF = float("inf")


def grid_to_adjacency_matrix(grid):
    rows = len(grid)
    cols = len(grid[0])

    def is_valid_cell(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != -1

    def get_weight(row, col):
        return grid[row][col] if is_valid_cell(row, col) else INF

    adjacency_matrix = [[INF for _ in range(rows * cols)] for _ in range(rows * cols)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == -1:
                continue  # Skip obstacles represented as -1
            current_node = r * cols + c
            adjacent_cells = [
                (r + dr, c + dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]
            ]
            for nr, nc in adjacent_cells:
                if is_valid_cell(nr, nc):
                    adjacent_node = nr * cols + nc
                    weight = get_weight(nr, nc)
                    adjacency_matrix[current_node][adjacent_node] = weight

    return adjacency_matrix


def floyd_warshall_distance1(graph, start, end):
    num_vertices = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph for storing distances

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Return the shortest distance between start and end
    return dist, []


INF = float("inf")


def floyd_warshall_with_path(graph):
    num_vertices = len(graph)
    dist = [
        [INF if i != j else 0 for j in range(num_vertices)] for i in range(num_vertices)
    ]
    next_hop = [[None for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Initialize distances and next_hop matrix
    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] != INF:
                next_hop[i][j] = j
            dist[i][j] = graph[i][j]

    # Floyd-Warshall algorithm with path reconstruction
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_hop[i][j] = next_hop[i][k]

    # Retrieve shortest paths
    shortest_paths = [[[] for _ in range(num_vertices)] for _ in range(num_vertices)]
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j and next_hop[i][j] is not None:
                path = [i]
                while path[-1] != j:
                    path.append(next_hop[path[-1]][j])
                shortest_paths[i][j] = path

    return dist, shortest_paths


# Example weighted graph (list of lists)
# Replace INF for absence of direct edge, weights for existing edges


def part1(file_name: str) -> int:
    grid = read_data(file_name=file_name)
    n, m = len(grid), len(grid[0])
    start_node = (0, 0)
    end_node = (n, m)
    g = grid_to_adjacency_matrix(grid)
    # print(g)
    result, path = floyd_warshall_with_path(g)
    print(path)
    print(result[0][-1])
    print(result[0][n * m - 1])
    print(path[0][m])
    # print(path)
    # print(result,d, paths)
    # print(path)


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
