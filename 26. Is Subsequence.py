class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Initialize two pointers for s and t
        i, j = 0, 0
        
        # Traverse through t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move s pointer
                i += 1
            j += 1  # Always move t pointer
        
        # If i reaches the end of s, it means s is a subsequence of t
        return i == len(s)
