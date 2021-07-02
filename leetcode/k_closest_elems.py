import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff_map = [[abs(num - x), num] for num in arr]
        diff_map.sort()
        res = [item[1] for item in diff_map[:k]]
        return sorted(res)


if __name__ == '__main__':
    arr = [int(num) for num in input("array: ").split()]
    k = int(input("Count of elements: "))
    x = int(input("Reference element: "))
    print(Solution().findClosestElements(arr, k, x))
