# coding: utf-8

from typing import List


class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:  # q4
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            return nums[(length - 1) // 2]
        else:
            i = length // 2
            return (nums[i - 1] + nums[i]) / 2


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1, 3], [2]))
