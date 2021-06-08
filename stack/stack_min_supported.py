from stack_max_supported import StackMaxSupported


class StackMinSupported(StackMaxSupported):

    def __str__(self):
        return self.items.__str__() + f' min item is {self.maxes.last()}'

    def push(self, item):
        self.items.push(item)
        self.maxes.push(item if self.maxes.size() == 0 or item < self.maxes.last() else self.maxes.last())
