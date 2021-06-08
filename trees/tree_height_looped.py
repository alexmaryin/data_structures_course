class Tree:
    def __init__(self, parents):
        self.parents = parents
        self.depths = {}
        self.max_height = 0

    def get_height(self, parent):
        if parent == -1:
            return 1
        if parent in self.depths.keys():
            return self.depths[parent] + 1
        else:
            return self.get_height(self.parents[parent]) + 1

    def height(self):
        for idx, parent in enumerate(self.parents):
            cur = self.get_height(self.parents[idx])
            self.depths[idx] = cur
            self.max_height = max(self.max_height, cur)
        return self.max_height


if __name__ == '__main__':
    nodes_count = int(input())
    parents = [int(i) for i in input().split()]
    assert nodes_count == len(parents) and nodes_count > 0
    tree = Tree(parents)
    print(tree.height())
