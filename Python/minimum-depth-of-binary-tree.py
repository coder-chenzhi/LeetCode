__author__ = 'chenzhi'

"""
Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

https://leetcode.com/problems/minimum-depth-of-binary-tree/

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
    def minDepth(self, root):
        # right answer
        if root is None:
            return 0
        elif root.left is None:
            return 1 + self.minDepth(root.right)
        elif root.right is None:
            return 1 + self.minDepth(root.left)
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        # wrong answer, pay attention to the definition of leaf node
        # if root is None:
        #     return 0
        # else:
        #     return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(1)
    root.left = node1
    print Solution().minDepth(root)