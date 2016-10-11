__author__ = 'chenzhi'

"""
Next Permutation

https://leetcode.com/problems/next-permutation/
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        if len(nums) == 0:
            return
        i = len(nums) - 1
        for i in reversed(range(1, len(nums))):
            if nums[i] > nums[i-1]:
                break
        if i == 1 and nums[i] <= nums[i-1]:
            i = 0
            j = len(nums)-1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1
            return

        for j in reversed(range(len(nums))):
            if nums[j] > nums[i - 1]:
                break
        tmp = nums[j]
        nums[j] = nums[i-1]
        nums[i-1] = tmp
        j = len(nums) - 1
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1

if __name__ == "__main__":
    nums = [1, 1, 5]
    Solution().nextPermutation(nums)
    print nums
