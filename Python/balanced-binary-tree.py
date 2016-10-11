__author__ = 'chenzhi'

"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

https://leetcode.com/problems/balanced-binary-tree/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        _, balanced = self.height(root)
        return balanced

    def height(self, root):
        if root is None:
            return 0, True
        else:
            left_height, left_balanced = self.height(root.left)
            right_height, right_balanced = self.height(root.right)
            # print left_height, right_height
            return max(left_height, right_height) + 1, \
                   abs(left_height - right_height) <= 1 and left_balanced and right_balanced

if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    root.left = node1
    root.right = node2
    print Solution().isBalanced(root)