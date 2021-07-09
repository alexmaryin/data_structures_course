from stack.stack import Stack


def solve(left: Stack[int], right: Stack[int], temp: Stack[int], n):
    if n == 1:
        right.push(left.pop())
    else:
        solve(left, temp, right, n - 1)
        solve(left, right, temp, 1)
        solve(temp, right, left, n - 1)


def main():
    discs_count = 4
    tower1: Stack[int] = Stack()
    tower2: Stack[int] = Stack()
    tower3: Stack[int] = Stack()
    for i in range(discs_count, 0, -1):
        tower1.push(i)
    print(tower1, tower2, tower3)
    solve(tower1, tower3, tower2, discs_count)
    print(tower1, tower2, tower3)


if __name__ == "__main__":
    main()
