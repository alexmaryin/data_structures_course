from queue import Queue


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


if __name__ == '__main__':
    main()
