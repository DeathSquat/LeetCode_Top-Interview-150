class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase and filter out non-alphanumeric characters
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Check if the filtered string is equal to its reverse
        return filtered_s == filtered_s[::-1]
