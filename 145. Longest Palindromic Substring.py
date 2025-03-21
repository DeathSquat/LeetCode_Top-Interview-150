class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(left, right):
            """
            Expand around the given center and return the longest palindrome
            substring found.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome
            return s[left + 1:right]

        if len(s) <= 1:
            return s

        longest_palindrome = ""
        for i in range(len(s)):
            # Odd-length palindrome (single character center)
            odd_palindrome = expand_around_center(i, i)
            # Even-length palindrome (two character center)
            even_palindrome = expand_around_center(i, i + 1)

            # Choose the longest among the current options
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome

        return longest_palindrome


# Example Usage
solution = Solution()

# Example 1
s1 = "babad"
print(solution.longestPalindrome(s1))  # Output: "bab" or "aba"

# Example 2
s2 = "cbbd"
print(solution.longestPalindrome(s2))  # Output: "bb"

# Example 3
s3 = "a"
print(solution.longestPalindrome(s3))  # Output: "a"

# Example 4
s4 = "ac"
print(solution.longestPalindrome(s4))  # Output: "a" or "c"
