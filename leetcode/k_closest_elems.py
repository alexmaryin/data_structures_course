import bisect
from typing import List


class Solution:
    def findClosestElementsNaive(self, arr: List[int], k: int, x: int) -> List[int]:
        diff_map = [[abs(num - x), num] for num in arr]
        diff_map.sort()
        res = [item[1] for item in diff_map[:k]]
        return sorted(res)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        left = bisect.bisect_left(arr, x) - 1
        right = left + 1
        while right - left - 1 < k:
            if left < 0:
                right += 1
                continue
            if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1:right]

    def findClosestElementsFastest(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]


if __name__ == '__main__':
    arr = [int(num) for num in input("array: ").split()]
    k = int(input("Count of elements: "))
    x = int(input("Reference element: "))
    print(Solution().findClosestElements(arr, k, x))
