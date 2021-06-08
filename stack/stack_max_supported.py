from stack.stack import Stack


class StackMaxSupported:
    def __init__(self):
        self.items = Stack()
        self.maxes = Stack()

    def __str__(self):
        return self.items.__str__() + f' max item is {self.maxes.last()}'

    def push(self, item):
        self.items.push(item)
        self.maxes.push(item if self.maxes.size() == 0 or int(item) > self.maxes.last() else self.maxes.last())

    def pop(self):
        self.maxes.pop()
        return self.items.pop()

    def max(self):
        return self.maxes.last()

    def size(self):
        return self.items.size()
