class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = len(arr)
        if l == 1:
            return arr[0]
        t = int(25 * l / 100)
        cur = -1
        count = 0
        for i in arr:
            if i == cur:
                count += 1
                if count > t:
                    return i
            else:
                count = 1
            cur = i