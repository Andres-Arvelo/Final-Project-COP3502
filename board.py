import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen

        removed = {"easy": 30, "medium": 40, "hard": 50}[difficulty]

        gen = SudokuGenerator(9, removed)
        gen.fill_values()
        self.solution = [row[:] for row in gen.get_board()]
        gen.remove_cells()
        self.board = [row[:] for row in gen.get_board()]
        self.original = [row[:] for row in self.board]

        # Creates the 81 Cells
        self.cells = []
        for r in range(9):
            row_cells = []
            for c in range(9):
                row_cells.append(Cell(self.board[r][c], r, c, screen))
            self.cells.append(row_cells)

        self.selected = None
        self.cell_size = width // 9


    def draw(self):
        # the grid background
        pygame.draw.rect(self.screen, (245, 245, 245),
                         (0, 0, self.width, self.height))

        for i in range(10):
            thick = 4 if i % 3 == 0 else 1
            pygame.draw.line(self.screen, (0, 0, 0),
                             (0, i * self.cell_size),
                             (self.width, i * self.cell_size,), thick)
            pygame.draw.line(self.screen, (0, 0, 0),
                             (i * self.cell_size, 0),
                             (i * self.cell_size, self.height), thick)

        # draws each cell
        for r in range(9):
            for c in range(9):
                self.cells[r][c].draw(self.cell_size)


    def select(self, row, col):
        if self.selected:
            old_r, old_c = self.selected
            self.cells[old_r][old_c].selected = False

        self.selected = (row, col)
        self.cells[row][col].selected = True

    def click(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return y // self.cell_size, x // self.cell_size
        return None

    def clear(self):
        if not self.selected:
            return

        r, c = self.selected
        cell = self.cells[r][c]

        if cell.editable:
            cell.value = 0
            cell.sketched_value = 0

    def sketch(self, value):
        if self.selected:
            r, c = self.selected
            self.cells[r][c].set_sketched_value(value)

    def place_number(self, value):
        if not self.selected:
            return False

        r, c = self.selected
        cell = self.cells[r][c]

        if cell.editable:
            cell.set_cell_value(value)
            cell.sketched_value = 0

        return True

    def reset_to_original(self):
        for r in range(9):
            for c in range(9):
                val = self.original[r][c]
                cell = self.cells[r][c]
                cell.value = val
                cell.sketched_value = 0
                cell.editable = (val == 0)

    def is_full(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return False
        return True

    def update_board(self):
        for r in range(9):
            for c in range(9):
                self.board[r][c] = self.cells[r][c].value

    def find_empty(self):
        for r in range(9):
            for c in range(9):
                if self.cells[r][c].value == 0:
                    return r, c
        return None

    def check_board(self):
        self.update_board()
        return self.board == self.solution
