import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        print(merged)
        median = len(merged) / 2
        print(median)
        if median - int(median) == 0:
            avg = (merged[round(median) - 1] + merged[round(median)]) / 2
        else:
            avg = merged[math.ceil(median) - 1]
        return avg


if __name__ == '__main__':
    nums1, nums2 = [1, 3], [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
