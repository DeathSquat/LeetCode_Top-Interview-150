class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        substring_len = word_len * word_count
        word_freq = {}

        # Build the frequency dictionary for the words
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        result = []

        # Iterate over the string
        for i in range(word_len):
            left = i
            right = i
            current_freq = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    current_freq[word] = current_freq.get(word, 0) + 1
                    count += 1

                    # If word frequency exceeds, move left pointer
                    while current_freq[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current_freq[left_word] -= 1
                        count -= 1
                        left += word_len

                    # Check if we have a valid substring
                    if count == word_count:
                        result.append(left)
                else:
                    # Reset pointers and frequencies
                    current_freq.clear()
                    count = 0
                    left = right

        return result
