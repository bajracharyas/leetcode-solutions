class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l = ""
        i = 0
        while True:
            c = ""
            broke = False
            for s in strs:
                if len(s) < i + 1:
                    broke = True
                    break
                if c == "":
                    c = s[i]
                elif s[i] != c:
                    broke = True
                    break
            if broke:
                break
            else:
                l += c
            i += 1
                    
        return l