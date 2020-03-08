# coding: utf-8

from typing import List
from class_def import ListNode
from prepare_input import gen_listnode, gen_listnode_list


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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:  # q23
        def add_to_list(given_list, given_listnode):
            while given_listnode.next:
                given_list.append(given_listnode)
                given_listnode = given_listnode.next
            given_list.append(given_listnode)

        ordered_list = []
        for listnode in lists:
            if not listnode:
                continue
            add_to_list(ordered_list, listnode)
        if len(ordered_list) == 0:
            return lists
        ordered_list.sort(key=lambda x: x.val)
        for i in range(len(ordered_list) - 1):
            ordered_list[i].next = ordered_list[i + 1]
        ordered_list[-1].next = None
        return ordered_list[0]


if __name__ == '__main__':
    solution = Solution()
    # print(solution.findMedianSortedArrays([1, 3], [2]))
    # print(solution.mergeKLists(gen_listnode_list([[1, 4, 5], [1, 3, 4], [2, 6]])))
