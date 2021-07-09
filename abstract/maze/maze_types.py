import random
from enum import Enum
from typing import NamedTuple, List


class Cell(str, Enum):
    EMPTY = ' '
    WALL = 'X'
    START = '#'
    GOAL = 'O'
    PATH = '.'


class MazePos(NamedTuple):
    row: int
    col: int


class Maze:
    def __init__(self, rows=10, cols=10, sparseness=0.2, start=MazePos(0, 0), goal=MazePos(9, 9)):
        self._rows = rows
        self._cols = cols
        self.start = start
        self.goal = goal
        self._grid = [[Cell.EMPTY for _ in range(cols)] for _ in range(rows)]
        self._build_walls(self._rows, self._cols, sparseness)
        self._grid[start.row][start.col] = Cell.START
        self._grid[goal.row][goal.col] = Cell.GOAL

    def _build_walls(self, rows, cols, sparseness):
        for row in range(rows):
            for col in range(cols):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][col] = Cell.WALL

    def __str__(self):
        header = '┌' + '─'*self._cols + '┐\n'
        footer = '└' + '─'*self._cols + '┘'
        body = ''
        for row in self._grid:
            body += '│' + ''.join([c.value for c in row]) + '│\n'
        return header + body + footer

    def is_goal(self, pos: MazePos):
        return pos == self.goal

    def successors(self, pos: MazePos) -> List[MazePos]:
        available = []
        if pos.row + 1 < self._rows and self._grid[pos.row + 1][pos.col] != Cell.WALL:
            available.append(MazePos(pos.row + 1, pos.col))
        if pos.row - 1 >= 0 and self._grid[pos.row - 1][pos.col] != Cell.WALL:
            available.append(MazePos(pos.row - 1, pos.col))
        if pos.col + 1 < self._cols and self._grid[pos.row][pos.col + 1] != Cell.WALL:
            available.append(MazePos(pos.row, pos.col + 1))
        if pos.col - 1 >= 0 and self._grid[pos.row][pos.col - 1] != Cell.WALL:
            available.append(MazePos(pos.row, pos.col - 1))
        return available

    def mark(self, path: List[MazePos]):
        for pos in path:
            self._grid[pos.row][pos.col] = Cell.PATH
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL

    def clear(self, path: List[MazePos]):
        for pos in path:
            self._grid[pos.row][pos.col] = Cell.EMPTY
        self._grid[self.start.row][self.start.col] = Cell.START
        self._grid[self.goal.row][self.goal.col] = Cell.GOAL

