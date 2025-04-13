from pprint import pprint
# returns the first empty grid case else false if full
def is_empty(grid) -> bool:
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return True
    return False


def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return i, j


# check if grid cell is a valid one row wise
def check_row(grid, num, row):
    if num in grid[row]:
        return False
    
    return True

# check if grid cell is a valid one col wise
def check_col(grid, num, col):
    if num in [grid[i][col] for i in range(len(grid))]:
        return False
        
    return True

# check if grid cell is a valid one box wise
def check_neighbor(grid, num, row, col):
    row_pos = (row // 3) * 3
    col_pos = (col // 3) * 3
    
    for i in range(row_pos, row_pos + 3):
        for j in range(col_pos, col_pos + 3):
            if grid[i][j] == num:
                return False
    
    return True
    
    
# backtracking Solver
def solver(grid):
    if (not is_empty(grid)):
        return True
    
    row, col = find_empty(grid)
    for i in range(1, 10):
        if (check_col(grid, i, col) and check_row(grid, i, row) and check_neighbor(grid, i, row, col)):
            grid[row][col] = i
            if solver(grid):
                return True
            grid[row][col] = 0
    
    return False
    
    
            
        

grid = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
        [2, 2, 3, 4, 5, 6, 7, 8, 9],
        [3, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 2, 3, 4, 5, 6, 7, 8, 9],
        [5, 2, 3, 4, 5, 6, 7, 8, 9],
        [6, 2, 3, 4, 5, 6, 7, 8, 9],
        [7, 2, 3, 4, 5, 6, 7, 8, 9],
        [8, 2, 3, 4, 5, 6, 7, 8, 9],
        [9, 2, 3, 4, 5, 6, 7, 8, 9]]

sudoku_grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 0, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

empty_grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
