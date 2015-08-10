__author__ = 'chenzhi'

"""
Rotate Array

Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

https://leetcode.com/problems/rotate-array/

"""


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        k %= len(nums)
        if k == 0:
            return
        tmp = []
        for i in range(k):
            tmp.append(nums[len(nums) - k + i])
        for i in range(len(nums) - k):
            nums[len(nums) - i - 1] = nums[len(nums) - k - i - 1]
        for i in range(k):
            nums[i] = tmp[i]

if __name__ == "__main__":
    nums = [1]
    Solution().rotate(nums, 3)
    print nums