__author__ = 'chenzhi'

"""
3Sum

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

https://leetcode.com/problems/3sum/

"""


class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            value = - nums[i]
            head = i + 1
            tail = len(nums) - 1
            while head < tail:
                if nums[head] + nums[tail] == value:
                    result.append([nums[i], nums[head], nums[tail]])
                    head += 1
                    while nums[head] == nums[head - 1] and head < tail:
                        head += 1
                elif nums[head] + nums[tail] < value:
                    head += 1
                else:
                    tail -= 1
        return result


if __name__ == "__main__":
    # print Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print Solution().threeSum([0, 0, 0, 0, 0])