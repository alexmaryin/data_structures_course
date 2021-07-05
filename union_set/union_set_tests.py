from union_set.tree_set import TreeSet

if __name__ == '__main__':
    ts = TreeSet()
    tables, queries = map(int, input().split())
    for idx, rec in enumerate(input().split()):
        ts.add(int(idx + 1), int(rec))
    assert len(ts.parents.keys()) == tables
    res = []
    for i in range(queries):
        first, second = map(int, input().split())
        ts.union(first, second)
        res.append(ts.max_table)
    for r in res:
        print(r)
