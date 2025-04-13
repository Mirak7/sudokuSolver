import tkinter as tk
from solver import solver

import tkinter as tk

CELL_SIZE = 50
GRID_SIZE = 9
BOX_SIZE = 3

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.master.configure(bg="white")
        self.canvas = tk.Canvas(master, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="white")
        self.canvas.pack()
        self.cells = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.draw_grid()
        self.create_cells()

        solve_btn = tk.Button(master, text="Solve", command=self.solve, bg="white", relief="flat")
        solve_btn.pack(fill='x', padx=10, pady=10)

    def draw_grid(self):
        for i in range(GRID_SIZE + 1):
            width = 3 if i % BOX_SIZE == 0 else 1
            # Vertical line
            self.canvas.create_line(i*CELL_SIZE, 0, i*CELL_SIZE, GRID_SIZE*CELL_SIZE, width=width)
            # Horizontal line
            self.canvas.create_line(0, i*CELL_SIZE, GRID_SIZE*CELL_SIZE, i*CELL_SIZE, width=width)

    def create_cells(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                entry = tk.Entry(self.master, width=2, font=('Arial', 18), justify='center', bd=0, bg="white")
                x = j * CELL_SIZE + CELL_SIZE // 2
                y = i * CELL_SIZE + CELL_SIZE // 2
                self.canvas.create_window(x, y, window=entry, width=CELL_SIZE - 5, height=CELL_SIZE - 5)
                self.cells[i][j] = entry

    def get_grid(self):
        grid = []
        for row in self.cells:
            grid_row = []
            for cell in row:
                val = cell.get()
                grid_row.append(int(val) if val.isdigit() else 0)
            grid.append(grid_row)
        return grid

    def fill_grid(self, grid):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

    def solve(self):
        grid = self.get_grid()
        if solver(grid):
            self.fill_grid(grid)
        else:
            print("No solution found")

# Insert your solver and helper functions here...