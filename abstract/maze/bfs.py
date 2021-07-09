from typing import TypeVar, Callable, List, Optional, Set

from abstract.maze.node import Node
from abstract.maze.queue import Queue

T = TypeVar('T')


def bfs(initial: T, is_goal: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Queue[Node[T]] = Queue()
    frontier.push(Node(initial, None))
    explored: Set[T] = {initial}

    while not frontier.is_empty:
        current_node: Node[T] = frontier.pop()
        current_state = current_node.state
        if is_goal(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None

