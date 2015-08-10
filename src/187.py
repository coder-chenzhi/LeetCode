__author__ = 'chenzhi'

"""
Repeated DNA Sequences

https://leetcode.com/problems/repeated-dna-sequences/

"""

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        if len(s) < 10:
            return []
        freq = {}
        for i in range(len(s) - 10 + 1):
            if s[i:i+10] in freq:
                freq[s[i:i+10]] += 1
            else:
                freq[s[i:i+10]] = 1
        return [k for k in freq if freq[k] > 1]


if __name__ == "__main__":
    print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")