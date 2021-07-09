from typing import TypeVar, Callable, List, Optional, Set
from abstract.maze.node import Node
from stack.stack import Stack

T = TypeVar('T')


def dfs(initial: T, is_goal: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    explored: Set[T] = {initial}

    while not frontier.is_empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if is_goal(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None


def node_to_path(node: Node[T]) -> List[T]:
    path = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
