__author__ = 'chenzhi'

"""
Sort List
Sort a linked list in O(n log n) time using constant space complexity.

https://leetcode.com/problems/sort-list/
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        copy = []
        cur = head
        while cur is not None:
            copy.append(cur)
            cur = cur.next

        def sort(a_head, a_tail):
            if a_head < a_tail:
                sort(a_head, (a_head + a_tail)/2)
                sort((a_head + a_tail)/2+1, a_tail)
                merge_list(a_head, (a_head + a_tail)/2, (a_head + a_tail)/2+1, a_tail)

        def merge_list(a_head, a_tail, b_head, b_tail):
            a_index = a_head
            b_index = b_head
            tmp = []
            while a_index <= a_tail and b_index <= b_tail:
                if copy[a_index].val < copy[b_index].val:
                    tmp.append(copy[a_index])
                    a_index += 1
                else:
                    tmp.append(copy[b_index])
                    b_index += 1
            if a_index <= a_tail:
                while a_index <= a_tail:
                    tmp.append(copy[a_index])
                    a_index += 1
            if b_index <= b_tail:
                while b_index <= b_tail:
                    tmp.append(copy[b_index])
                    b_index += 1
            for i in range(len(tmp)):
                copy[a_head + i] = tmp[i]
            # printArrayList(copy)

        sort(0, len(copy)-1)
        for i in range(len(copy) - 1):
            copy[i].next = copy[i+1]
        copy[-1].next = None
        return copy[0]


def printArrayList(array):
    for element in array:
        print element.val,
    print ""

def printList(head):
    tmp = head
    while tmp != None:
        print tmp.val,
        tmp = tmp.next
    print ""

if __name__ == "__main__":
    first = ListNode(5)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(1)
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    printList(first)
    head = Solution().sortList(first)
    printList(head)