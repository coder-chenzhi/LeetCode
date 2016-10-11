__author__ = 'chenzhi'

"""
Fraction to Recurring Decimal

https://leetcode.com/problems/fraction-to-recurring-decimal/
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        string = ""
        if numerator * denominator < 0:
            string = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator == 0:
            string += str(numerator / denominator)
        else:
            string += str(numerator / denominator) + "."
            chushu = []
            shang = []
            reminder = numerator % denominator * 10
            chushu.append(numerator % denominator)
            shang.append(reminder / denominator)
            reminder %= denominator
            while reminder not in chushu:
                if reminder == 0:
                    for i in range(len(shang)):
                        string += str(shang[i])
                    return string
                chushu.append(reminder)
                reminder *= 10
                shang.append(reminder / denominator)
                reminder %= denominator
            else:
                index = chushu.index(reminder)
                for i in range(index):
                    string += str(shang[i])
                string += '('
                for i in range(index, len(shang)):
                    string += str(shang[i])
                string += ')'

        return string


if __name__ == "__main__":
    print Solution().fractionToDecimal(-1, -8)