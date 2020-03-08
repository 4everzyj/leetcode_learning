# coding: utf-8

from class_def import ListNode


def gen_listnode(num_list):
    last_listnode = None
    for num in num_list[::-1]:
        listnode = ListNode(num)
        listnode.next = last_listnode
        last_listnode = listnode
    return last_listnode


def gen_listnode_list(input_list):
    listnode_list = []
    for num_list in input_list:
        listnode_list.append(gen_listnode(num_list))
    return listnode_list


if __name__ == '__main__':
    res = gen_listnode_list([[1, 4, 5], [1, 3, 4], [2, 6]])
