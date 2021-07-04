from typing import List


def number_rank(num) -> int:
    step = num
    rank = 1
    while step >= 10:
        step /= 10
        rank += 1
    return rank


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cns = 0
        step = 0
        for num in nums:
            if num == 1:
                step += 1
            else:
                max_cns = max(max_cns, step)
                step = 0
        return max(max_cns, step)

    def findNumbers(self, nums: List[int]) -> int:
        return len(list(filter(lambda x: number_rank(x) % 2 == 0, nums)))

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])


if __name__ == '__main__':
    s = Solution()
    nums = [1, 0, 1, 1, 0, 1]
    assert s.findMaxConsecutiveOnes(nums) == 2
    nums = [12, 345, 2, 6, 7896]
    assert s.findNumbers(nums) == 2
