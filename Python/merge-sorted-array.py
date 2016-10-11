__author__ = 'chenzhi'
"""
Merge Sorted Array

https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge_solution_one(self, nums1, m, nums2, n):
        # move the elements of nums1
        for i in reversed(range(m)):
            nums1[i + n] = nums1[i]

        # merge
        i = n
        j = 0
        k = 0
        while i < n + m and j < n:
            if nums1[i] < nums2[j]:
                nums1[k] = nums1[i]
                k += 1
                i += 1
            else:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        if j < n:
            while j < n:
                nums1[k] = nums2[j]
                k += 1
                j += 1

    def merge(self, nums1, m, nums2, n):
        l1, l2, end = m-1, n-1, m+n-1
        while l1 >= 0 and l2 >= 0:
            if nums2[l2] > nums1[l1]:
                nums1[end] = nums2[l2]
                l2 -= 1
            else:
                nums1[end] = nums1[l1]
                l1 -= 1
            end -= 1
        if l1 < 0:  # if nums2 left
            nums1[:l2+1] = nums2[:l2+1]


if __name__ == "__main__":
    m = 5
    nums1 = [1, 4, 9, 10, 15, 0, 0, 0]
    n = 3
    nums2 = [9, 12, 17]
    # m = 0
    # nums1 = []
    # n = 0
    # nums2 = []
    Solution().merge(nums1, m, nums2, n)
    print nums1