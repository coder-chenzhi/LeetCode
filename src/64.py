__author__ = 'chenzhi'

"""
Minimum Path Sum

https://leetcode.com/problems/minimum-path-sum/

"""

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        minPath = []
        minPath.append([grid[0][0]])
        for i in range(1, len(grid[0])):
            minPath[0].append(minPath[0][i - 1] + grid[0][i])
        for i in range(1, len(grid)):
            minPath.append([minPath[i - 1][0] + grid[i][0]])
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                minPath[i].append(min(minPath[i][j-1], minPath[i-1][j]) + grid[i][j])
        return minPath[-1][-1]

if __name__ == "__main__":
    # grid = [[1,2,3,4], [4,2,3,4], [1,2,3,4]]
    grid = [[1]]
    print Solution().minPathSum(grid)