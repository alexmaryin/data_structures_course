from queue2s_max import Queue2sMaxSupported

if __name__ == '__main__':
    count = int(input())
    items = [int(i) for i in input().split()]
    window_size = int(input())
    maxes = []

    window = Queue2sMaxSupported()
    for i in range(window_size):
        window.enqueue(items[i])
    maxes.append(window.max())
    for i in range(window_size, count):
        window.enqueue(items[i])
        window.dequeue()
        maxes.append(window.max())
    print(*maxes)
