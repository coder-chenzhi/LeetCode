__author__ = 'chenzhi'

"""
Jump Game

https://leetcode.com/problems/jump-game/

"""

class Solution(object):
    def canJump_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = [False] * len(nums)
        reachable[-1] = True
        for i in reversed(range(len(nums)-1)):
            for j in range(i, min(len(nums), i + nums[i] + 1)):
                reachable[i] = reachable[i] or reachable[j]
                if reachable[i]:
                    break
        return reachable[0]

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable = [False] * len(nums)
        reachable[-1] = True
        for i in reversed(range(len(nums)-1)):
            if nums[i] == 0:
                continue
            if nums[i] < nums[i+1]:
                reachable[i] = reachable[i+1]
            else:
                reachable[i] = reachable[i] or reachable[i+1]
                for j in range(min(len(nums), i + nums[i+1] + 1), min(len(nums), i + nums[i] + 1)):
                    reachable[i] = reachable[i] or reachable[j]
                    if reachable[i]:
                        break
        return reachable[0]



if __name__ == "__main__":
    print Solution().canJump([3,2,1,0,4])