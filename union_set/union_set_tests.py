from union_set.tree_set import TreeSet1
from union_set.vars_set import VarSet


def first_task():
    ts = TreeSet1()
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


def second_task():
    max_val, eq, deq = map(int, input().split())
    res = 1
    parents = {}
    for _ in range(eq):
        first, second = map(int, input().split())
        if first not in parents.keys():
            parents[first] = first
        if second not in parents.keys():
            parents[second] = parents[first]
    for _ in range(deq):
        first, second = map(int, input().split())
        if first not in parents.keys():
            parents[first] = first
        if second not in parents.keys():
            parents[second] = second
        if parents[first] == parents[second]:
            res = 0
    return res


if __name__ == '__main__':
    print(second_task())
