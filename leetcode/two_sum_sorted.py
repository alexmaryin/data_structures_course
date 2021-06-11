from typing import List
import bisect


def two_sum(numbers: List[int], target: int) -> List[int]:
    for i, v in enumerate(numbers):
        completed = target - v
        sug = bisect.bisect_left(numbers[i+1:], completed) + i + 1
        if sug < len(numbers) and numbers[sug] == completed:
            return [i, sug]
    return []


def two_sum_fastest(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [left, right]
    return []


if __name__ == '__main__':
    # inp = [2, 7, 11, 15]
    inp = [0, 0, 3, 4]
    target = 0
    a, b = map(int, two_sum_fastest(inp, target))
    print(a, b)
    assert target == inp[a] + inp[b]
