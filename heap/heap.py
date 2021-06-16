import math
from typing import List


class HeapItem:
    def __init__(self, priority: int, data):
        self.priority: int = priority
        self.data = data


def parent_id(idx):
    return math.floor(idx / 2)


def left_id(idx):
    return idx * 2 + 1


def right_id(idx):
    return idx * 2 + 2


class HeapMax:
    def __init__(self, source: List[int] = None):
        if source:
            self.data: List[HeapItem] = [HeapItem(i, None) for i in source]
        else:
            self.data: List[HeapItem] = []

    def __str__(self):
        return '-'.join([str(item.priority) for item in self.data])

    def parent(self, idx):
        return self.data[parent_id(idx)]

    def left(self, idx):
        return self.data[left_id(idx)]

    def right(self, idx):
        return self.data[right_id(idx)]

    def size(self):
        return len(self.data)

    def swap(self, idx1, idx2):
        if idx1 <= self.size() and idx2 <= self.size():
            self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        else:
            raise IndexError("Heap size is less than indices for swap")

    def sift_up(self, idx):
        i = idx
        while i > 0 and self.parent(i).priority < self.data[i].priority:
            self.swap(i, parent_id(i))
            i = parent_id(i)

    def sift_down(self, idx):
        max_idx = idx
        left_idx, right_idx = left_id(idx), right_id(idx)
        if left_idx < self.size() and self.data[left_idx].priority > self.data[max_idx].priority:
            max_idx = left_idx
        if right_idx < self.size() and self.data[right_idx].priority > self.data[max_idx].priority:
            max_idx = right_idx
        if idx != max_idx:
            self.swap(idx, max_idx)
            self.sift_down(max_idx)

    def insert(self, item: HeapItem):
        self.data.append(item)
        self.sift_up(self.size() - 1)

    def remove(self, idx):
        self.data[idx].priority = self.data[0].priority + 1
        self.sift_up(idx)
        self.get_item_max()

    def get_item_max(self):
        if self.size() > 0:
            result = self.data[0]
            if self.size() > 1:
                self.data[0] = self.data.pop()
                self.sift_down(0)
            return result
        else:
            return None

    def change_priority(self, idx, new_priority: int):
        old_priority, self.data[idx].priority = self.data[idx].priority, new_priority
        if new_priority > old_priority:
            self.sift_up(idx)
        else:
            self.sift_down(idx)
