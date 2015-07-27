"""
Candy

https://leetcode.com/problems/candy/

"""


class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        totalCandy = 0
        trends = []
        increase = 'all equal'
        count = 1
        equalLists = []
        equalList = []
        equalCount = 0
        equalStart = 0

        if len(ratings) == 1:
            return 1
        # decide first trend
        for i in range(len(ratings) - 1):
            if ratings[i] != ratings[i + 1]:
                increase = ratings[i] < ratings[i + 1]
                break
        if increase == 'all equal':
            return len(ratings)

        # traverse list to get trends
        for i in range(len(ratings) - 1):
            if ratings[i] == ratings[i + 1]:
                if equalCount == 0:
                    equalStart = count
                equalCount += 1
            else:
                if equalCount != 0:
                    equalList.append((equalStart, equalCount))
                    equalCount = 0
                if (ratings[i] < ratings[i + 1]) == increase:
                    count += 1
                else:
                    trends.append(self.trendToSign(increase) * count)
                    equalLists.append(equalList)
                    equalList = []
                    count = 2
                    increase = not increase
        trends.append(self.trendToSign(increase) * count)
        equalLists.append(equalList)
        print trends
        print equalLists

        if trends[0] < 0:
            totalCandy += self.cumulativeSum(abs(trends[0])) - 1
            totalCandy += self.handleEqual(abs(trends[0]), False, equalLists[0])
        if trends[len(trends) - 1] > 0:
            totalCandy += self.cumulativeSum(abs(trends[len(trends) - 1])) - 1
            totalCandy += self.handleEqual(abs(trends[len(trends) - 1]), True, equalLists[len(equalLists) - 1])
        print totalCandy
        for i in range(len(trends) - 1):
            if trends[i] > 0:
                if trends[i] > abs(trends[i + 1]):
                    totalCandy += self.cumulativeSum(trends[i])
                    totalCandy += self.handleEqual(trends[i], True, equalLists[i])
                    print totalCandy
                    totalCandy += self.cumulativeSum(abs(trends[i + 1]) - 1)
                    totalCandy += self.handleEqual(abs(trends[i + 1]), False, equalLists[i + 1]) # pay attention to here
                    print totalCandy
                else:
                    print 'stub', totalCandy
                    totalCandy += self.cumulativeSum(trends[i] - 1)
                    totalCandy += self.handleEqual(trends[i] - 1, True, equalLists[i])
                    print 'wired', totalCandy
                    totalCandy += self.cumulativeSum(abs(trends[i + 1]))
                    totalCandy += self.handleEqual(abs(trends[i + 1]), False, equalLists[i + 1]) # pay attention to here
                    print totalCandy
                totalCandy -= 1
                print totalCandy
        totalCandy += 1
        print 'totalCandy', totalCandy
        return totalCandy

    def trendToSign(self, increase):
        if increase:
            return 1
        else:
            return -1

    def handleEqual(self, maxValue, increase, equalList):
        num = 0
        for item in equalList:
            if increase:
                num += item[0] * item[1]
            else:
                num += (maxValue - (item[0] - 1)) * item[1]
        return num

    def cumulativeSum(self, num):
        return num * (num + 1) / 2

if __name__ == '__main__':
    s = Solution()
    #s.candy([6,4,1,2,3,4,5,6,7,5,5,4,3,2,1,2,2,4,3,2,1,1,3])
    print s.candy([0])