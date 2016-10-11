__author__ = 'chenzhi'

"""
Maximum Gap
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
Try to solve it in linear time/space.

https://leetcode.com/problems/maximum-gap/
"""

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        max_value = max(nums)
        min_value = min(nums)
        division = (max_value - min_value) / (len(nums)+1) + 1
        buckets = []
        difference = 0
        for _ in range(len(nums)+1):
            buckets.append([])
        for i in nums:
            buckets[(i-min_value)/division].append(i)
        start_emtry = []
        strike_emtry = -1
        i = 0
        last_unempty = 0
        for i in reversed(range(len(buckets))):
            if len(buckets[i]) != 0:
                last_unempty = i
                break

        i = 0
        while i < last_unempty+1:
            if len(buckets[i]) == 0:
                tmp_start = i
                tmp_strike = 1
                i += 1
                while i < last_unempty+1 and len(buckets[i]) == 0:
                    tmp_strike += 1
                    i += 1
                if tmp_strike > strike_emtry:
                    start_emtry = [tmp_start]
                    strike_emtry = tmp_strike
                elif tmp_strike == strike_emtry:
                    start_emtry.append(tmp_start)
            else:
                i += 1

        for start in start_emtry:
            tmp_diff = min(buckets[start+strike_emtry]) - max(buckets[start-1])
            difference = max(difference, tmp_diff)

        return difference

if __name__ == "__main__":
    # print Solution().maximumGap([1,2,3,4,5,6,8,20])
    # print Solution().maximumGap([1,1,1,1,1,5,5,5,5,5])
    print Solution().maximumGap([1,1,1,1,1])