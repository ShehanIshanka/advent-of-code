def is_valid_cell(grid, visited, row, col):
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and not visited[row][col]


def find_paths(grid, start, end, path, paths, visited):
    rows, cols = len(grid), len(grid[0])
    row, col = start

    path.append(start)
    visited[row][col] = True

    if start == end:
        paths.append(list(path))
    else:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if is_valid_cell(grid, visited, new_row, new_col):
                find_paths(grid, (new_row, new_col), end, path, paths, visited)

    path.pop()
    visited[row][col] = False


# Example grid represented as a list of lists
grid = [[0] * 13 for i in range(13)]

start_node = (0, 0)  # Replace with your start node coordinates
end_node = (12, 12)  # Replace with your end node coordinates

visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
all_paths = []

find_paths(grid, start_node, end_node, [], all_paths, visited)

# Display all paths
for path in all_paths:
    print(path)
