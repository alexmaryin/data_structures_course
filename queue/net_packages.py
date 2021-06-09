from buffered_queue import BufferedQueue


class Processor:
    def __init__(self, buffer_limit):
        self.buffer = BufferedQueue(buffer_limit)
        self.time = 0

    def check_for_time(self, time):
        if self.buffer.size() == 0:
            return True
        while self.buffer.size() > 0 and self.buffer.next() <= time:
            self.buffer.dequeue()
        return True if self.buffer.size() < self.buffer.limit else False

    def enqueue(self, arrival, duration):
        if self.check_for_time(arrival):
            time = max(arrival, self.buffer.last() or self.time)
            print(time)
            self.buffer.enqueue(time + duration)
            self.time = time + duration
        else:
            print(-1)


if __name__ == '__main__':
    limit, count = map(int, input().split())
    if count > 0:
        packages = [map(int, input().split()) for _ in range(count)]
        processor = Processor(limit)
        for idx, package in enumerate(packages):
            processor.enqueue(next(package), next(package))
