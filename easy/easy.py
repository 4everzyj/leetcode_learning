# coding: utf-8

from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # q1 20200310
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums:
                diff_i = nums.index(diff)
                if diff_i != i:
                    return [i, diff_i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
