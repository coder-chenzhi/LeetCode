__author__ = 'chenzhi'

"""
Reverse Nodes in k-Group

https://leetcode.com/problems/reverse-nodes-in-k-group/

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
    def reverseKGroup_slow_version(self, head, k):
        if head is None:
            return head
        group_first = head
        pre = self
        pre.next = head
        while True:
            # check has more than k elements left
            for _ in range(k):
                if group_first.next is not None:
                    group_first = group_first.next
                else:
                    return self.next

            for i in reversed(range(1, k)):
                self.swap_pair_k(pre, i)

            for _ in range(k):
                pre = pre.next
        return self.next

    def swap_pair_k(self, pre, k):
        head = pre
        for _ in range(k):
            head = self.swapPair(head)
            head = head.next
        return pre

    # @param {ListNode} pre previous node of head
    # @param {ListNode} head
    # swap head and head.next
    def swapPair(self, pre):
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        return pre


    def reverseKGroup(self, head, k):
        if head is None:
            return head
        pre = self
        pre.next = head
        last = pre
        while True:
            # check has more than k elements left
            for _ in range(k):
                if last.next is not None:
                    last = last.next
                else:
                    return self.next

            group = []
            pointer = pre
            for _ in range(k):
                group.append(pointer.next)
                pointer = pointer.next
            pre.next = group[-1]
            group[0].next = group[-1].next
            last = group[0]
            for i in reversed(range(1, k)):
                group[i].next = group[i - 1]

            for _ in range(k):
                pre = pre.next
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
    head = Solution().reverseKGroup(first, 2)
    # head = Solution().swapPair(head)
    printList(head)