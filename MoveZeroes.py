class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for elt in nums:
            if elt != 0:
                nums[i] = elt
                i += 1
        while i < len(nums):
            nums[i] = 0
            i += 1