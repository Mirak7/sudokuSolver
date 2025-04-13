from solver import is_empty, check_col, check_neighbor, check_row, solver
from grids import sudoku_grid, empty_grid
from pprint import pprint
import tkinter as tk
from sudokuGUI import SudokuGUI

root = tk.Tk()
app = SudokuGUI(root)
root.mainloop()