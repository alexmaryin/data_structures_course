import math
from typing import List
from heap import HeapMax, HeapItem


def heap_sort(source: List[int]) -> List[int]:
    heap = HeapMax()
    for i in source:
        heap.insert(HeapItem(i, None))
    return [heap.get_item_max().priority for _ in range(heap.size())]


def build_heap(source: List[int]):
    heap = HeapMax(source)
    for i in reversed(range(heap.size() // 2)):
        heap.sift_up(i)
    return heap


# TODO Don't work correctly!!
def heap_sort2(source: List[int]) -> List[int]:
    heap = build_heap(source)
    for i in reversed(range(heap.size()-1)):
        heap.swap(0, i)
        heap.sift_down(0)
    return [item.priority for item in heap.data]
