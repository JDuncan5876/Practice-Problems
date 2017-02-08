"""
Find words that can be typed using only one row of a standard QWERTY keyboard
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
        row2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
        row3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        rows = [row1, row2, row3]
        wordsOnRow = []
        for word in words:
            oneRow = True
            lowWord = word.lower()
            for i in range(3):
                if lowWord[0] in rows[i]:
                    index = i
            for i in range(1, len(lowWord)):
                oneRow = oneRow and lowWord[i] in rows[index]
            if oneRow:
                wordsOnRow.append(word)
        return wordsOnRow