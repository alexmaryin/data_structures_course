from abstract.maze.astar import a_star
from abstract.maze.bfs import bfs
from abstract.maze.dfs import dfs, node_to_path
from abstract.maze.heuristics import manhattan_distance
from abstract.maze.maze_types import Maze, MazePos

if __name__ == "__main__":
    maze = Maze(100, 100, 0.3, MazePos(0, 0), MazePos(99, 99))
    solution_dfs = dfs(maze.start, maze.is_goal, maze.successors)
    solution_bfs = bfs(maze.start, maze.is_goal, maze.successors)
    dist = manhattan_distance(maze.goal)
    solution_a_star = a_star(maze.start, maze.is_goal, maze.successors, dist)
    for solution in [solution_dfs, solution_bfs, solution_a_star]:
        if solution:
            path = node_to_path(solution)
            maze.mark(path)
            # print(maze)
            print(f'Total {len(path)} steps.')
            maze.clear(path)
        else:
            print('Path not found!')
