from typing import TypeVar, Callable, List, Optional, Dict
from abstract.maze.node import Node
from abstract.maze.priority_queue import PriorityQueue

T = TypeVar('T')


def a_star(
        initial: T,
        is_goal: Callable[[T], bool],
        successors: Callable[[T], List[T]],
        heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(initial, None, 0.0, heuristic(initial)))
    explored: Dict[T, float] = {initial: 0.0}

    while not frontier.is_empty:
        current_node: Node[T] = frontier.pop()
        current_state = current_node.state
        if is_goal(current_state):
            return current_node
        for child in successors(current_state):
            new_cost = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child)))
    return None
