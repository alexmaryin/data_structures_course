import math
from typing import List


class SortHeapMax:
    def __init__(self, source: List[int]):
        self.heap = source
        self.swap_count = 0
        self.swap_list = []
        self.build_heap()

    def build_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.sift_up(i)
        print(f'Heap after build: {self.heap}')

    def sift_up(self, idx):
        i, parent = idx, math.floor(idx / 2) - 1
        while i > 0 and self.heap[parent] > self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.swap_count += 1
            self.swap_list.append([i, parent])
            i = parent

    def sift_down(self, idx):
        n_max = idx
        left, right = idx * 2, idx * 2 + 1
        if left < len(self.heap) and self.heap[left] > self.heap[n_max]:
            n_max = left
        if right < len(self.heap) and self.heap[right] > self.heap[n_max]:
            n_max = right
        if idx != n_max:
            self.heap[n_max], self.heap[idx] = self.heap[idx], self.heap[n_max]
            self.swap_count += 1
            self.swap_list.append([idx, n_max])
            self.sift_down(n_max)

    def sort(self):
        for i in range(1, len(self.heap), -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.sift_down(0)

    def sort_max(self):
        self.sort()
        self.heap.reverse()


def fast_heap_sort(source: List[int]):
    heap = SortHeapMax(source)
    heap.sort()
    return heap


class SortHeapMin:
    def __init__(self, source: List[int]):
        self.heap = source
        self.swap_count = 0
        self.swap_list = []
        self.build_heap()

    def build_heap(self):
        for i in reversed(range(len(self.heap) // 2)):
            self.sift_down(i)
        # print(f'Heap after build: {self.heap}')

    def sift_down(self, idx):
        n_max = idx
        left, right = idx * 2 + 1, idx * 2 + 2
        if left < len(self.heap) and self.heap[left] < self.heap[n_max]:
            n_max = left
        if right < len(self.heap) and self.heap[right] < self.heap[n_max]:
            n_max = right
        if idx != n_max:
            self.heap[n_max], self.heap[idx] = self.heap[idx], self.heap[n_max]
            self.swap_count += 1
            self.swap_list.append([idx, n_max])
            self.sift_down(n_max)


if __name__ == '__main__':
    count = int(input())
    array = [int(num) for num in input().split()]
    assert count == len(array)
    heap = SortHeapMin(array)
    print(heap.swap_count)
    for swap in heap.swap_list:
        print(*swap)
