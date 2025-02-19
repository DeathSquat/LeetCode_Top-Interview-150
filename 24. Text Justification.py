class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, line, line_length = [], [], 0

        for word in words:
            if line_length + len(line) + len(word) > maxWidth:  # Check if adding word exceeds maxWidth
                for i in range(maxWidth - line_length):
                    line[i % (len(line) - 1 or 1)] += ' '  # Distribute spaces
                res.append(''.join(line))  # Store justified line
                line, line_length = [], 0  # Reset for new line
            line.append(word)
            line_length += len(word)

        # Last line: left-justified, fill remaining space with spaces
        res.append(' '.join(line).ljust(maxWidth))
        return res
