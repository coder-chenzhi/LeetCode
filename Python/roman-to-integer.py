__author__ = 'chenzhi'

"""
Roman to Integer

Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.
https://leetcode.com/problems/roman-to-integer/

"""

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        charToValue = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sumInt = charToValue[s[0]]
        for i in range(len(s) - 1):
            if charToValue[s[i]] >= charToValue[s[i+1]]:
                sumInt += charToValue[s[i+1]]
            else:
                sumInt += charToValue[s[i+1]] - 2 * charToValue[s[i]]
        return sumInt


if __name__ == "__main__":
    print Solution().romanToInt("MCMLXXXIV")

