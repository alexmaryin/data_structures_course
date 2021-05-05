import sys
import numpy as np


def main():
    equations, variables = map(int, input().split())
    inputs = np.array([list(map(int, input().split())) for _ in range(0, equations)])
    print(inputs)
    left = inputs[:, :-1]
    print(left)
    right = inputs[:, -1]
    print(right)
    x, residuals, rank, s = np.linalg.lstsq(left, right, rcond=-1)
    print(*x, *residuals)


if __name__ == '__main__':
    main()
