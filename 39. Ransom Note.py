from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Count character frequencies in both strings
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Check if magazine has enough characters for ransomNote
        for char, count in ransom_count.items():
            if magazine_count[char] < count:
                return False
        
        return True
