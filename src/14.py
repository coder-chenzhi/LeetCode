__author__ = 'chenzhi'

"""
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

https://leetcode.com/problems/longest-common-prefix/

"""

class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        minLengh = min([len(s) for s in strs])
        for i in range(minLengh):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][0:i]
        return strs[0][0:minLengh]


if __name__ == "__main__":
    strs = ["abc", "abd", "a"]
    print Solution().longestCommonPrefix(strs)
