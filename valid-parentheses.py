class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        o = ["(", "{", "["]
        c = [")", "}", "]"]
        d = {"(": ")", "{": "}", "[": "]"}
        for i in s:
            if i in o:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if d[stack.pop()] != i:
                        return False
                
                
        if len(stack) == 0:
            return True
        else:
            return False
        