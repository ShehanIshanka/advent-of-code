# https://adventofcode.com/2023/day/17
from typing import Dict, List, Set
import sys

sys.setrecursionlimit(100000000)


def print_grid(grid):
    for x in grid:
        print("   ".join(map(str, x)))
        # print("".join(map(lambda x: "#" if len(x) > 0 else "O", x)))


def read_data(file_name: str) -> Dict[str, List[Set[int]]]:
    with open(file_name, "r") as file:
        data = file.read()

    cards = []
    for row in data.split("\n"):
        cards.append(list(map(int, list(row))))

    return cards


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
    flat = [item for sublist in grid for item in sublist]

    def is_valid_cell(row, col):
        return 0 <= row < rows and 0 <= col < cols and grid[row][col] != -1

    def get_weight(row, col):
        return grid[row][col] if is_valid_cell(row, col) else INF

    adjacency_matrix = [[INF for _ in range(rows * cols)] for _ in range(rows * cols)]
    print(flat)
    for r in range(rows):
        for c in range(cols):
            # if r == c:
            #     val = 0  # Skip obstacles represented as -1
            # else:
            #     current_node = r * cols + c - 1
            #     print(r,c,current_node)
            #     val = flat[current_node]
            adjacency_matrix[r][c + 1] = grid[r][c]
            # adjacency_matrix[r+1][c] = grid[r][c]

    return adjacency_matrix


def is_valid_path(path):
    # print(path)
    if len(path) < 3:
        return True
    h = []

    node = path[0]
    for a in path[1:]:
        if abs(a[0] - node[0]) == 0 and abs(a[1] - node[1]) == 1:
            h.append("ROW")
        elif abs(a[0] - node[0]) == 1 and abs(a[1] - node[1]) == 0:
            h.append("COL")
        else:
            h.append("TURN")
        node = a
        print(h, set(h), path)
        if len(h) > 2 and len(set(h[-3:])) == 1 and h[-1] in ["COL", "ROW"]:
            return False

    return True


def floyd_warshall_distance(graph):
    num_vertices = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph for storing distances
    paths = [
        [[(row, i)] for i in range(num_vertices)] for row in range(num_vertices)
    ]  # Create a copy of the graph for storing distances

    # Floyd-Warshall algorithm
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # if dist[i][k] + dist[k][j] < dist[i][j] and is_valid_path(paths[i][k] + paths[k][j]):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    paths[i][j] = paths[i][k] + paths[k][j]

    # Return the shortest distance between start and end
    return dist


def floyd_warshall_distance1(graph):
    n, m = len(graph), len(graph[0])
    dist = graph  # Create a copy of the graph for storing distances
    paths = [
        [[(row, col)] for col in range(m)] for row in range(n)
    ]  # Create a copy of the graph for storing distances

    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # if i == j:
                #     dist[i][j] = graph[i][j]
                #     continue
                # if dist[i][k] + dist[k][j] < dist[i][j] and is_valid_path(paths[i][k] + paths[k][j]):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    paths[i][j] = paths[i][k] + paths[k][j]

    # Return the shortest distance between start and end
    return dist, paths


INF = float("inf")


def floyd_warshall(grid):
    num_nodes = len(grid)
    dist = [[INF for _ in range(num_nodes)] for _ in range(num_nodes)]

    for i in range(num_nodes):
        for j in range(num_nodes):
            if i == j:
                dist[i][j] = 0
            elif abs(i - j) == 1:
                dist[i][j] = grid[i][j]

    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist, []


def part1(file_name: str) -> int:
    grid = [
        [1111, 2, 3],
        [11, 121, 13],
        [21, 22, 21],
        # [31,32,33,34],
    ]
    # grid = read_data(file_name=file_name)
    # n, m = len(grid), len(grid[0])
    # print(n,m)
    # start_node = (0, 0)
    # end_node = (n,m)
    # g = grid_to_adjacency_matrix(grid)
    result, paths = floyd_warshall(grid)
    print_grid(paths)
    print("=" * 100)
    print_grid(result)
    print(result[0][-1])


if __name__ == "__main__":
    print(part1(file_name="test.txt"))  # 13
    # print(part1(file_name="input.txt"))  # 20667
    #
    # print(part2(file_name="test.txt"))  # 30
    # print(part2(file_name="input.txt"))  # 5833065
