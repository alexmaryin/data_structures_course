import heapq
from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        m, n = max(row, col), min(row, col)
        row_larger = True if row > col else False
        res = None
        for x in range(n + 1):
            each = [0] * m
            for y in range(x, 0, -1):
                for z in range(m):
                    each[z] += matrix[z][y] if row_larger else matrix[y][z]
                res = max(res, self.largest_sum_close(each, k))
                if res == k:
                    return res
        return res

    def largest_sum_close(self, each, k):
        sum = 0
        heap = [0]
        heapq.heapify(heap)
        for i in range(len(each)):
            sum +=




if __name__ == '__main__':
    matrix = [[1, 0, 1],
              [0, -2, 3]]
    matrix2 = [[2, 2, -1]]
    k = 2
    print(Solution().maxSumSubmatrix(matrix, k))

