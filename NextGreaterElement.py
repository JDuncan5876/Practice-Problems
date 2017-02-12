# Given findNums, a subset of nums, for each element of findNums get the next larger element in nums (nums does not contain duplicates)
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        nextGreaters = []
        numsDict = {}
        for i in range(len(nums)):
            numsDict[nums[i]] = i
        for num in findNums:
            nextGreater = -1
            for i in range(numsDict[num] + 1, len(nums)):
                if nums[i] > num:
                    nextGreater = nums[i]
                    break
            nextGreaters.append(nextGreater)
        return nextGreaters
