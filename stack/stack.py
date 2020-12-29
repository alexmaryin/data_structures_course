class Stack:
    def __init__(self):
        self.list = []

    def push(self, item):
        self.list.insert(0, item)

    def pop(self):
        if self.list:
            item = self.list[0]
            self.list = self.list[1:]
            return item
        else:
            return None

    def last(self):
        if self.list:
            return self.list[0]
        else:
            return None

    def size(self):
        return len(self.list)
