"""
3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

https://leetcode.com/problems/3sum-closest/
"""


class Solution:
    def __init__(self):
        pass

    def sign(self, num):
        if num == 0:
            return 0
        elif num > 0:
            return 1
        else:
            return -1

    def twoSumClosest(self, num, end, target):
        print "target =", target
        start = 0
        pre = num[start] + num[end]
        if pre == target:
            return pre
        elif pre > target:
            end -= 1
        else:
            start += 1
        now = num[start] + num[end]
        # print "now =", num[start] , "+", num[end]
        while now != target:
            if now > target:
                end -= 1
            else:
                start += 1
            if start < end:
                pre = now
                # print "now =", num[start] , "+", num[end]
                now = num[start] + num[end]
            else:
                break
        if now == target:
            return target
        elif abs(now - target) > abs(pre - target):
            return pre
        else:
            return now

    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        if result >= target:
            return result
        # print result
        for i in range(3, len(num)):
            tmp = num[i] + self.twoSumClosest(num, i - 1, target - num[i])

            if tmp == target:
                return target
            if abs(result - target) > abs(tmp - target):
                result = tmp
            # print result
        return result

s = Solution()
print s.threeSumClosest([1,2,4,8,16,32,64,128], 82)