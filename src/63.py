__author__ = 'chenzhi'

"""
Unique Paths II

https://leetcode.com/problemset/algorithms/
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        matrix = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for _ in range(m):
            matrix.append([0]*n)
        for i in range(n):
            if obstacleGrid[0][i] == 0:
                matrix[0][i] = 1
            else:
                break

        for j in range(m):
            if obstacleGrid[j][0] == 0:
                matrix[j][0] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

        return matrix[-1][-1]


if __name__ == "__main__":
    # print Solution().uniquePathsWithObstacles([[0,0,0], [0,1,0], [0,0,0]])
    # print Solution().uniquePathsWithObstacles([[1,1,1],[0,0,0]])
    print Solution().uniquePathsWithObstacles([[0,1], [0,0]])