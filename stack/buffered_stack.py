class BufferedStack:
    def __init__(self, buffer):
        self.list = []
        self.buffer = int(buffer)

    def __str__(self):
        return self.list.__str__() + f' with buffer {self.buffer}'

    def push(self, item):
        if self.size() < self.buffer:
            self.list.append(int(item))
            return True
        else:
            return False

    def pop(self):
        if self.list:
            return self.list.pop()
        else:
            return None

    def last(self):
        if self.list:
            return self.list[self.size() - 1]
        else:
            return None

    def size(self):
        return len(self.list)
