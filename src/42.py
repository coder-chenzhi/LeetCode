__author__ = 'chenzhi'

"""
Trapping Rain Water

https://leetcode.com/problems/trapping-rain-water/
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        peak = [0]
        for i in range(1, len(height)-1):
            
        peak.append(len(height)-1)


if __name__ == "__main__":
    print Solution().trap([])