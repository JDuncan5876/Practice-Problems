"""
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
"""

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0: return [0]
        out = [0, 1]
        for power in range(1, n):
            base = 2 ** power
            for i in range(base, base * 2):
                lastIndex = 2 * base - 1 - i;
                out.append(base + out[lastIndex])
        return out