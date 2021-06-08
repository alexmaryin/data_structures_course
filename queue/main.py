import random

from queue import Queue
from queue_on_stacks import Queue2s
from utils.time_measuring import measured_time


def main():
    queue = Queue()
    is_exit = False
    while not is_exit:
        raw = input("Enter command (q(enqueue) #value / dq(dequeue) / size / p(rint) / e(xit): ").split()
        if raw:
            command = raw[0]
            if command == 'e':
                is_exit = True
            elif command == 'q':
                queue.enqueue(raw[1])
                print(f"Value {raw[1]} append to queue")
            elif command == 'dq':
                n = queue.dequeue()
                if n:
                    print(f"Got next value {n} from queue")
                else:
                    print("Queue is empty!")
            elif command == 'size':
                print(f'Queue size is {queue.size()} items')
            elif command == "p":
                print(queue)


@measured_time
def big_queue_test(queue, count):
    print(f"Enqueue {count} items")
    for i in range(count - 1):
        queue.enqueue(i)
    print(f"Dequeue {count} items")
    for i in range(count - 1):
        queue.dequeue()


if __name__ == '__main__':
    items = 100000
    print("Simple queue")
    big_queue_test(Queue(), items)
    print("Queue on stacks")
    big_queue_test(Queue2s(), items)
