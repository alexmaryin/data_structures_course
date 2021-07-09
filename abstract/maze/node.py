from __future__ import annotations
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost=0.0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other: Node):
        return self.cost + self.heuristic < other.cost + other.heuristic
