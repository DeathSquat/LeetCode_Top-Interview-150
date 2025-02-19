class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()  # To keep track of unique characters in the current substring
        left = 0  # Left pointer for the sliding window
        max_length = 0  # To store the length of the longest substring
        
        for right in range(len(s)):
            # If the character at the right pointer is already in the set,
            # move the left pointer to remove characters until it's no longer in the set
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            # Add the current character to the set
            char_set.add(s[right])
            
            # Update the maximum length of the substring
            max_length = max(max_length, right - left + 1)
        
        return max_length
