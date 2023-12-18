def flood_fill(grid, row, col, target_color, replacement_color):
    rows, cols = len(grid), len(grid[0])

    if (
        row < 0
        or col < 0
        or row >= rows
        or col >= cols
        or grid[row][col] != target_color
    ):
        return

    grid[row][col] = replacement_color

    # Recursively fill neighboring cells
    flood_fill(grid, row + 1, col, target_color, replacement_color)
    flood_fill(grid, row - 1, col, target_color, replacement_color)
    flood_fill(grid, row, col + 1, target_color, replacement_color)
    flood_fill(grid, row, col - 1, target_color, replacement_color)


# Example grid represented as a list of lists
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

# Starting position for flood fill
start_row, start_col = 1, 2

# Target color at starting position
target_color = grid[start_row][start_col]

# Replacement color for flood fill
replacement_color = 2

# Apply flood fill from the starting position
flood_fill(grid, start_row, start_col, target_color, replacement_color)

# Display the updated grid after flood fill
for row in grid:
    print(row)
