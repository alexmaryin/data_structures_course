from heap import HeapMin

if __name__ == '__main__':
    n, m = map(int, input().split())
    tasks = [int(time) for time in input().split()]
    assert m == len(tasks)
    heap = HeapMin(n)
    print(heap.data)
    for task in tasks:
        proc = heap.data[0]['proc']
        time = heap.data[0]['time']
        heap.data[0]['time'] += task
        heap.sift_down(0)
        print(proc, time)
