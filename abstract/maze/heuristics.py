from math import sqrt
from typing import Callable
from abstract.maze.maze_types import MazePos


def euclidean_distance(goal: MazePos) -> Callable[[MazePos], float]:
    def distance(pos: MazePos) -> float:
        x_dist = pos.col - goal.col
        y_dist = pos.row - goal.row
        return sqrt((x_dist * x_dist) + (y_dist * y_dist))
    return distance


def manhattan_distance(goal: MazePos) -> Callable[[MazePos], float]:
    def distance(pos: MazePos) -> float:
        x_dist = abs(pos.col - goal.col)
        y_dist = abs(pos.row - goal.row)
        return x_dist + y_dist
    return distance
