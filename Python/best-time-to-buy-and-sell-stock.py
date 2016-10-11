__author__ = 'chenzhi'

"""
Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution(object):
    def maxProfit_slow(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        low_value = []
        low_index = []
        low_value.append(prices[0])
        low_index.append(0)
        for i in range(1, len(prices)-1):
            if prices[i] <= prices[i-1] and prices[i] <= prices[i+1]:
                low_value.append(prices[i])
                low_index.append(i)
        low_value.append(prices[-1])
        low_index.append(len(prices)-1)

        profit = max(prices[low_index[0]:len(prices)]) - low_value[0]
        for i in range(1, len(low_index)):
            if prices[low_index[i]] >= prices[low_index[i-1]]:
                continue
            else:
                profit = max(profit, max(prices[low_index[i]:len(prices)])-low_value[i])
        return profit

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        lowest_value = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit = max(profit, prices[i] - lowest_value)
            lowest_value = min(lowest_value, prices[i])
        return profit


if __name__ == "__main__":
    print Solution().maxProfit([6,1,3,2,4,7])
    print Solution().maxProfit([3,3,5,0,0,3,1,4])
