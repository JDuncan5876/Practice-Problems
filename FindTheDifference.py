class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sLetters = {}
        for c in s:
            if c not in sLetters:
                sLetters[c] = 0
            sLetters[c] += 1
        for c in t:
            if c in sLetters and sLetters[c] > 0:
                sLetters[c] -= 1
            else:
                return c
