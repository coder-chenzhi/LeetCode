__author__ = 'chenzhi'
"""
Rotate List

https://leetcode.com/problems/rotate-list/

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
        if head is None:
            return head
        size = 1
        first = head
        while first.next is not None:
            size += 1
            first = first.next
        if k % size == 0:
            return head
        movement = size - (k % size)
        first.next = head
        for _ in range(movement):
            first = first.next
        head = first.next
        first.next = None
        return head


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
    fifth = ListNode(5)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    printList(first)
    head = Solution().rotateRight(first, 9)
    printList(head)