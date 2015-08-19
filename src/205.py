__author__ = 'chenzhi'

"""
Isomorphic Strings

https://leetcode.com/problems/isomorphic-strings/
"""


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        s_to_t = {}
        t_to_s = {}
        for i in range(len(s)):
            if s[i] in s_to_t:
                if s_to_t[s[i]] != t[i]:
                    return False

            if t[i] in t_to_s:
                if t_to_s[t[i]] != s[i]:
                    return False

            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        return True

if __name__ == "__main__":
    print Solution().isIsomorphic("paper", "title")