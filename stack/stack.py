class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.append(item)

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
