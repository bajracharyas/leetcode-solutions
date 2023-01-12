class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def isPalindromeString(s):
            if len(s) <= 1:
                return True
            return s[0] == s[-1] and isPalindromeString(s[1:-1])
        
        return isPalindromeString(str(x))