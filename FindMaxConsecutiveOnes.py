class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            if count > maxCount:
                maxCount = count
        return maxCount
