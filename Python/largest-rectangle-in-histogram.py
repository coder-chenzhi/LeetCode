__author__ = 'chenzhi'

"""
Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

https://leetcode.com/problems/largest-rectangle-in-histogram/
Similar Problem: Maximal Rectangle(85)

"""


class Solution:
    # @param {integer[]} height
    # @return {integer}
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
    print Solution().largestRectangleArea([2,1,5,6,2,3])
