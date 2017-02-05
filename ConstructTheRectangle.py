class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = int(area ** 0.5)
        while area % width != 0:
            width -= 1
        return [area / width, width]