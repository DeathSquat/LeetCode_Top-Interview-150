from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)  # Convert wordList to a set for O(1) lookups
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, transformation is impossible
        
        queue = deque([(beginWord, 1)])  # Queue stores (current word, transformation steps)
        
        while queue:
            word, steps = queue.popleft()
            
            if word == endWord:
                return steps  # Found the shortest transformation sequence
            
            # Generate all possible next words by changing one character at a time
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch != word[i]:  # Ensure at least one letter changes
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in wordSet:
                            queue.append((newWord, steps + 1))
                            wordSet.remove(newWord)  # Remove to prevent revisits
        
        return 0  # No valid transformation sequence found
