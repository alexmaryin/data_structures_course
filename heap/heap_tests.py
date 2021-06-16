import random
from heap import HeapMax, HeapItem

if __name__ == '__main__':
    heap = HeapMax()
    items_priority = [15, 12, 9, 14, 8, 3, 7, 13, 11, 5]
    items_priority2 = [3, 3, 3, 5, 5, 5, 0, 9]
    random.shuffle(items_priority2)
    for idx, priority in enumerate(items_priority2):
        heap.insert(HeapItem(priority, f'item {idx + 1}'))
    print(heap)
