from typing import Dict


class TreeSet:
    def __init__(self):
        self.parents: Dict[int, int] = {}
        self.ranks: Dict[int, int] = {}
        self.counts: Dict[int, int] = {}
        self.max_table = 0

    def __repr__(self): return f'Parents: {self.parents}\nRanks:   {self.ranks}'
    def __str__(self): return self.__repr__()

    def add(self, item: int, records: int):
        self.parents[item] = item
        self.ranks[item] = 0
        self.counts[item] = records
        self.max_table = max(self.max_table, records)

    def find(self, item):
        if item != self.parents[item]:
            self.parents[item] = self.find(self.parents[item])
        return self.parents[item]

    def get_max(self):
        return self.max_table

    def union(self, first, second):
        first_parent, second_parent = self.find(first), self.find(second)
        if first_parent == second_parent:
            return
        if self.ranks[first_parent] > self.ranks[second_parent]:
            self.parents[second_parent] = first_parent
            self.counts[first_parent] += self.counts[second_parent]
        else:
            self.parents[first_parent] = second_parent
            self.counts[second_parent] += self.counts[first_parent]
            if self.ranks[first_parent] == self.ranks[second_parent]:
                self.ranks[second_parent] += 1
        self.max_table = max(self.max_table, self.counts[first_parent], self.counts[second_parent])
