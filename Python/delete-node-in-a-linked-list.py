__author__ = 'chenzhi'

"""
Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/

"""

import copy

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def printList(head):
    tmp = head
    while tmp != None:
        print tmp.val,
        tmp = tmp.next
    print ""


if __name__ == "__main__":
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    first.next = second
    second.next = third
    third.next = fourth
    printList(first)
    Solution().deleteNode(third)
    printList(first)