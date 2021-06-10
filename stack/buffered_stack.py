from stack.stack import Stack


class BufferedStack(Stack):
    def __init__(self, buffer):
        super().__init__()
        self.buffer = int(buffer)

    def __str__(self):
        return self.list.__str__() + f' with buffer {self.buffer}'

    def push(self, item):
        if self.size() < self.buffer:
            self.list.append(int(item))
            return True
        else:
            return False
