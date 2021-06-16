import random
from heapq import heapify

from heap import HeapMax, HeapItem
from heap_sort import heap_sort, heap_sort2
from utils.time_measuring import measured_time


@measured_time
def sort1(source):
    return heap_sort(source)


@measured_time
def sort2(source):
    return heap_sort2(source)


@measured_time
def sort3(source):
    heapify(source)
    source.sort()
    return source


def test_simple():
    heap = HeapMax()
    items_priority = [15, 12, 9, 14, 8, 3, 7, 13, 11, 5]
    items_priority2 = [3, 3, 3, 5, 5, 5, 0, 9]
    random.shuffle(items_priority)
    for idx, priority in enumerate(items_priority):
        heap.insert(HeapItem(priority, f'item {idx + 1}'))
        print(heap)


if __name__ == '__main__':
    array = [random.randint(0, 200) for _ in range(10000)]
    print("First method:")
    res = sort1(array)
    print(res[:100])
    print("Second method:")
    res = sort2(array)
    print(res[:100])
    print("Third method:")
    res = list(reversed(sort3(array)))
    print(res[:100])
