import tkinter as tk
from solver import solver

class SudokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.cells = [[None for _ in range(9)] for _ in range(9)]

        self.create_grid()
        self.create_solve_button()

    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.master, width=3, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j, padx=2, pady=2)
                self.cells[i][j] = entry

    def create_solve_button(self):
        solve_btn = tk.Button(self.master, text="Solve", command=self.solve)
        solve_btn.grid(row=9, column=0, columnspan=9, sticky="we", pady=10)

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
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                self.cells[i][j].insert(0, str(grid[i][j]))

    def solve(self):
        grid = self.get_grid()
        if solver(grid):
            self.fill_grid(grid)
        else:
            print("No solution exists.")

# Your solver and helper functions go below