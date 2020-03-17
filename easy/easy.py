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

    def reverse(self, x: int) -> int:  # q7 20200317
        x_str = str(x)
        if x_str[0] == '-':
            new_str = x_str[0] + x_str[1:][::-1]
        else:
            new_str = x_str[::-1]
        if int(new_str) < -2 ** 31 or int(new_str) > 2 ** 31 - 1:
            return 0
        return int(new_str)


if __name__ == '__main__':
    solution = Solution()
    # print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.reverse(-1230))
