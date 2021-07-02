import random
from heapq import heapify

from heap import HeapMax, HeapItem
from fast_heap_sort import fast_heap_sort
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


@measured_time
def sort_4(source):
    return fast_heap_sort(source)


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
    print("Fourth method:")
    res = sort_4(array)
    print(res[:100])
