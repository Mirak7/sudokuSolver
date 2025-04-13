# returns the first empty grid case else false if full
def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ".":
                return i, j
    return False


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

def check_neighbor(grid, num, row, col):
    row_pos = (row // 3) * 3
    col_pos = (col // 3) * 3
    
    for i in range(row_pos + 3):
        for j in range(col_pos + 3):
            if grid[i][j] == num:
                return False
    
    return True


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
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

print(check_neighbor(sudoku_grid, 2, 1, 1))
#print(check_valid(sudoku_grid))
