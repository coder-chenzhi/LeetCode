__author__ = 'chenzhi'

"""
Maximal Rectangle
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

https://leetcode.com/problems/maximal-rectangle/
"""

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        if not isinstance(matrix[0], list):
            return self.largestRectangleArea([int(i) for i in matrix])
        length = len(matrix[0])
        width = len(matrix)
        height = [0] * length
        maxArea = 0
        for i in range(width):
            for j in range(length):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            # print height
            maxArea = max(maxArea, self.largestRectangleArea(height))
        return maxArea

    def largestRectangleArea(self, height):
        length = len(height)
        stack = []
        maxArea = 0
        i = 0
        while i <= length:
            h = 0
            if i != length:
                h = height[i]
            if len(stack) == 0 or h >= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                tp = stack.pop()
                if len(stack) == 0:
                    maxArea = max(maxArea, height[tp] * i)
                else:
                    maxArea = max(maxArea, height[tp] * (i-1-stack[-1]))
        return maxArea


if __name__ == "__main__":
    print Solution().maximalRectangle([["0", "1", "1", "1"], ["1", "1", "0", "0"],
                                       ["1", "0", "1", "1"], ["1", "0", "1", "1"]])
    # print Solution().maximalRectangle(["1"])
