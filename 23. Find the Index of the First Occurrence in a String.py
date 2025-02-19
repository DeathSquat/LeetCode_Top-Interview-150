class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Check if needle is empty
        if not needle:
            return 0
        
        # Loop through haystack and check for the first occurrence of needle
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # If needle is not found, return -1
        return -1
