"""
Candy

https://leetcode.com/problems/candy/

"""


class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        # use two pass scan from left to right and vice versa to keep the candy level up to now
        # similar to like the Trapping Rain Water question
        res = [1]*len(ratings) # also compatable with [] input
        lbase = rbase = 1
        # left scan
        for i in xrange(1, len(ratings)):
            lbase = lbase + 1 if ratings[i] > ratings[i-1] else 1
            res[i] = lbase
        # right scan
        for i in xrange(len(ratings)-2, -1, -1):
            rbase = rbase + 1 if ratings[i] > ratings[i+1] else 1
            res[i] = max(rbase, res[i])
        return sum(res)

if __name__ == '__main__':
    s = Solution()
    print s.candy([6,4,1,2,3,4,5,6,7,5,5,4,3,2,1,2,2,4,3,2,1,1,3])