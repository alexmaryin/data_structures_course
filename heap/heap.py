class HeapMin:
    def __init__(self, proc_count):
        self.data = [{'time': 0, 'proc': i} for i in range(proc_count)]

    def swap(self, idx1, idx2):
        if idx1 <= len(self.data) and idx2 <= len(self.data):
            self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        else:
            raise IndexError("Heap size is less than indices for swap")

    def child_less(self, idx, child):
        if child >= len(self.data):
            return False
        if self.data[child]['time'] < self.data[idx]['time']:
            return True
        if self.data[child]['time'] == self.data[idx]['time'] and self.data[child]['proc'] < self.data[idx]['proc']:
            return True
        return False

    def sift_down(self, idx):
        min_idx = idx
        left_idx, right_idx = idx * 2, idx * 2 + 1
        if self.child_less(min_idx, left_idx):
            min_idx = left_idx
        if self.child_less(min_idx, right_idx):
            min_idx = right_idx
        if idx != min_idx:
            self.swap(idx, min_idx)
            self.sift_down(min_idx)
