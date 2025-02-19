class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)  # Sort citations in descending order
        h = 0  # Initialize h-index

        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1  # Update h-index
            else:
                break  # Stop when citations[i] < i + 1

        return h
