class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary(object):
    
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        
    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self._search_in_node(word, self.root)
    
    def _search_in_node(self, word, node):
        for i, char in enumerate(word):
            if char == '.':
                for child in node.children.values():
                    if self._search_in_node(word[i+1:], child):
                        return True
                return False
            elif char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("word")
# param_2 = obj.search("pattern")
