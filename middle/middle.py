# coding: utf-8

from class_def import ListNode
from prepare_input import gen_listnode


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  # q2 20200310
        curr_node1 = l1
        curr_node2 = l2
        num1 = l1.val
        num2 = l2.val
        new_head = None
        last_node = None
        carry = 0
        bit_num = 1
        while curr_node1 or curr_node2:
            curr_sum = num1 + num2 + carry
            carry = curr_sum // 10
            sum_node = ListNode(curr_sum % 10)
            if bit_num == 1:
                new_head = sum_node
            else:
                last_node.next = sum_node
            last_node = sum_node
            num1 = 0
            num2 = 0
            if curr_node1:
                curr_node1 = curr_node1.next
                if curr_node1:
                    num1 = curr_node1.val
            if curr_node2:
                curr_node2 = curr_node2.next
                if curr_node2:
                    num2 = curr_node2.val
            bit_num += 1
        if carry == 1:
            last_node.next = ListNode(1)
        return new_head


if __name__ == '__main__':
    solution = Solution()
    res = solution.addTwoNumbers(gen_listnode([1]), gen_listnode([9, 9]))
