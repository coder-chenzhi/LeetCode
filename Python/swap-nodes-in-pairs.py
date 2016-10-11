__author__ = 'chenzhi'

"""
Swap Nodes in Pairs
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

https://leetcode.com/problems/swap-nodes-in-pairs/

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs_my_solution(self, head):
        if head is None or head.next is None:
            return head
        a = head
        b = head.next
        a.next = b.next
        b.next = a
        head = b

        a = head
        b = head.next
        before = None
        if a.next.next is None or b.next.next is None:
            return head

        before = b
        while a.next.next is not None and b.next.next is not None:
            # exchange
            a = a.next.next
            b = b.next.next
            a.next = b.next
            b.next = a
            before.next = b
            # fix order
            tmp = a
            a = b
            b = tmp
            before = b

        return head

    def swapPairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a
        return self.next


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
    sixth = ListNode(6)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    printList(first)
    head = Solution().swapPairs(first)
    printList(head)
