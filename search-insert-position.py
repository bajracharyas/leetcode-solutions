class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1:
            if target > nums[0]:
                return 1
            else:
                return 0
        medianIndex = len(nums) // 2
        if nums[medianIndex] == target:
            return medianIndex
        elif nums[medianIndex] > target:
            return self.searchInsert(nums[:medianIndex], target)
        elif nums[medianIndex] < target:
            return medianIndex + self.searchInsert(nums[medianIndex:], target)