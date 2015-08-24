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
        if len(height) == 0 or len(height) == 1:
            return 0
        max_value = max(height)
        max_index = 0
        peak = []
        stack = []
        water = 0
        if height[0] > height[1]:
            peak.append(0)

        for i in range(1, len(height)-1):
            if height[i] >= height[i-1] and height[i] >= height[i+1]:
                peak.append(i)

        if height[-1] > height[-2]:
            peak.append(len(height)-1)


        if len(peak) == 0:
            return 0

        for i in range(len(peak)):
            if height[peak[i]] == max_value:
                max_index = i
                break

        for i in range(max_index+1):
            if len(stack) == 0:
                stack.append(peak[i])
            elif height[peak[i]] >= height[stack[-1]]:
                v = height[stack[-1]]
                for j in range(stack[-1], peak[i]):
                    if v > height[j]:
                        water += v - height[j]
                stack.pop(-1)
                stack.append(peak[i])

        stack = []
        for i in reversed(range(max_index, len(peak))):
            if len(stack) == 0:
                stack.append(peak[i])
            elif height[peak[i]] >= height[stack[-1]]:
                v = height[stack[-1]]
                for j in range(peak[i]+1, stack[-1]):
                    if v > height[j]:
                        water += v - height[j]
                stack.pop(-1)
                stack.append(peak[i])

        return water


if __name__ == "__main__":
    print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
    print Solution().trap([5,5,1,7,1,1,5,2,7,6])
    print Solution().trap([0,1,0])