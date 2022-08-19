"""
Power sets
Details: https://en.wikipedia.org/wiki/Power_set
"""
from typing import List


def backtrack(_level: int, init: int, combination: List[int]):
    if _level == len(combination):
        print('Adding combination to result %s' % combination)
        result.append(list(combination))  # Add a deepcopy here to avoid empty lists in the result
        return

    for i in range(init, n):
        combination.append(nums[i])
        backtrack(_level, i+1, combination)
        combination.pop()


if __name__ == '__main__':
    nums: List[int] = [1, 2, 3, 4]
    n: int = len(nums)
    result: List[List[int]] = []

    for level in range(0, n+1):
        backtrack(_level=level, init=0, combination=[])

    print('Result: %s' % result)
