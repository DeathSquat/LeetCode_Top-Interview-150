class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  # Return empty string if the list is empty

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate through the rest of the strings
        for string in strs[1:]:
            # Reduce the prefix while it is not a prefix of the current string
            while not string.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:
                    return ""  # Return empty string if no common prefix exists

        return prefix
