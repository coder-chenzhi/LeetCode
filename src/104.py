__author__ = 'chenzhi'

"""
Maximum Depth of Binary Tree
Given a binary tree, find its maximum depth.

https://leetcode.com/problems/maximum-depth-of-binary-tree/

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if root is None:
            return 0
        elif root.left is None:
            return 1 + self.maxDepth(root.right)
        elif root.right is None:
            return 1 + self.maxDepth(root.left)
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    root.left = node1
    node1.right = node2
    print Solution().maxDepth(root)