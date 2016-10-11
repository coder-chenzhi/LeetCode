__author__ = 'chenzhi'

"""
Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


def printList(head):
    tmp = head
    while tmp != None:
        print tmp.val,
        tmp = tmp.next
    print ""


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        if head == None:
            return None
        now = head
        while now.next != None:
            if now.next.val == val:
                now.next = now.next.next
            else:
                now = now.next
        if head.val == val:
            return head.next
        else:
            return head

if __name__ == "__main__":
    # table = [1, 2, 6, 3, 4, 5, 6]
    table = [1]
    first = ListNode(table[0])
    now = first
    for i in range(1, len(table)):
        now.next = ListNode(table[i])
        now = now.next
    printList(first)
    Solution().removeElements(first, 2)
    printList(first)