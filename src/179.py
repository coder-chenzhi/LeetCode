__author__ = 'chenzhi'

"""
Largest Number

https://leetcode.com/problems/largest-number/
"""

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if max(nums) == 0:
            return "0"
        max_length = len(str(max(nums))) * 2  # a little trick
        nums = sorted(nums, key=lambda num: self.extend_to_length(str(num), max_length), reverse=True)
        nums = [str(s) for s in nums]
        return "".join(nums)

    def extend_to_length(self, num, length):
        """

        :param num: str
        :param length:
        :return:
        """
        times = length / len(num) + 1
        return (num * times)[:length]


if __name__ == "__main__":
    # print Solution().extend_to_length("123", 3)
    print Solution().largestNumber([3, 30, 34, 5, 9])