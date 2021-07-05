from typing import Dict


class VarSet:
    def __init__(self):
        self.parents: Dict[int, int] = {}
        self.ranks: Dict[int, int] = {}

    def add(self, *args):
        for item in args:
            self.parents[item] = item
            self.ranks[item] = 0

    def find(self, item):
        if item != self.parents[item]:
            self.parents[item] = self.find(self.parents[item])
        return self.parents[item]

    def is_equal(self, first, second):
        return self.find(first) == self.find(second)

    def union(self, first, second):
        first_parent, second_parent = self.find(first), self.find(second)
        if first_parent == second_parent:
            return
        if self.ranks[first_parent] > self.ranks[second_parent]:
            self.parents[second_parent] = first_parent
        else:
            self.parents[first_parent] = second_parent
            if self.ranks[first_parent] == self.ranks[second_parent]:
                self.ranks[second_parent] += 1
