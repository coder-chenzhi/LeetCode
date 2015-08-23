__author__ = 'chenzhi'

"""
Unique Paths

https://leetcode.com/problems/unique-paths/
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = []
        matrix.append([1]*n)
        for _ in range(m-1):
            matrix.append([1])
        for i in range(1, m):
            for j in range(1, n):
                matrix[i].append(matrix[i][-1] + matrix[i-1][j])

        return matrix[m-1][n-1]


if __name__ == "__main__":
    print Solution().uniquePaths(100, 100)