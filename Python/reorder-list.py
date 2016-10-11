__author__ = 'chenzhi'

"""
Reorder List

https://leetcode.com/problems/reorder-list/

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head is None:
            return
        tmp = []
        size = 0
        cur = head
        while cur is not None:
            tmp.append(cur)
            cur = cur.next
            size += 1

        cur = head
        for i in range(size / 2):
            reverse_cur = tmp[size - i - 1]
            next = cur.next
            cur.next = reverse_cur
            reverse_cur.next = next
            cur = next

        tmp[size / 2].next = None


def printList(head):
    tmp = head
    while tmp != None:
        print tmp.val,
        tmp = tmp.next
    print ""


if __name__ == "__main__":
    first = ListNode(1)
    # second = ListNode(2)
    # third = ListNode(3)
    # fourth = ListNode(4)
    # fifth = ListNode(5)
    # first.next = second
    # second.next = third
    # third.next = fourth
    # fourth.next = fifth
    printList(first)
    Solution().reorderList(None)
    printList(first)