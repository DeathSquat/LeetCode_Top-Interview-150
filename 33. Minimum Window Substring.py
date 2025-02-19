from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)  # Number of unique chars in t to be matched
        
        # Pointers and tracking variables
        left, right = 0, 0
        formed = 0
        window_count = {}
        
        # Result tuple: (window length, left index, right index)
        ans = float("inf"), None, None
        
        while right < len(s):
            # Add current character to the window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if character is a required one and if its count matches in t
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to shrink the window from the left
            while left <= right and formed == required:
                char = s[left]
                
                # Update the result if we found a smaller valid window
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove leftmost character from the window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1  # Move left pointer
            
            right += 1  # Expand window from the right
        
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
