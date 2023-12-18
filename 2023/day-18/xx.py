def calculate_inner_area(grid):
    rows, cols = len(grid), len(grid[0])
    inner_area = 0

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 0:
                inner_area += 1

    return inner_area


# Example grid represented as a list of lists with ones representing the boundary of the polygon
grid = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

inner_polygon_area = calculate_inner_area(grid)
print(f"Area of the inner polygon: {inner_polygon_area}")
