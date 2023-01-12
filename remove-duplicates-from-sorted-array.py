class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 1
        c = nums[0]
        while i < l:
            if nums[i] == c:
                l -= 1
                del nums[i]
            else:
                c = nums[i]
                i += 1
        return l
            
        