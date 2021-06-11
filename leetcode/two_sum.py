from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_map(nums: List[int], target: int) -> List[int]:
    hash = {v: k for k, v in enumerate(nums)}
    for i in range(len(nums)):
        complete = target - nums[i]
        if complete in hash and hash[complete] != i:
            return [i, hash[complete]]
    return []


if __name__ == '__main__':
    inp = [2, 7, 11, 15]
    target = 9
    a, b = map(int, two_sum(inp, target))
    print(a, b)
    assert target == inp[a] + inp[b]
    a, b = map(int, two_sum_map(inp, target))
    print(a, b)
    assert target == inp[a] + inp[b]
