from buffered_queue import BufferedQueue


class Processor:
    def __init__(self, buffer):
        self.buffer = BufferedQueue(buffer)
        self.time = 0

    def add(self, arrival, duration):
        self.time = max(self.buffer.next() or 0, arrival)
        if self.buffer.enqueue(self.time + duration):
            return self.time
        else:
            while self.buffer.size() > 0 and self.buffer.next() <= arrival:
                self.buffer.dequeue()
            if self.buffer.enqueue(self.time + duration):
                return self.time
        return -1


if __name__ == '__main__':
    limit, count = map(int, input().split())
    if count > 0:
        packages = [map(int, input().split()) for _ in range(count)]
        processor = Processor(limit)
        for idx, package in enumerate(packages):
            arrival, duration = next(package), next(package)
            print(processor.add(arrival, duration))
