def build_tree(root, nodes):
    children = [build_tree(child, nodes) for child, node in enumerate(nodes) if node == root]
    return {'key': root, 'children': children}


def height(tree):
    return max((height(sub_tree) for sub_tree in tree['children']), default=-1) + 1


if __name__ == '__main__':
    nodes_count = int(input())
    nodes = [int(i) for i in input().split()]
    assert nodes_count == len(nodes) and nodes_count > 0
    tree = build_tree(-1, nodes)
    print(height(tree))
