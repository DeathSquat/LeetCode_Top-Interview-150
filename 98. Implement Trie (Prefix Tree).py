class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end = False  # Marks the end of a valid word

class Trie(object):

    def __init__(self):
        """
        Initialize the Trie object.
        """
        self.root = TrieNode()  # Root node of the Trie

    def insert(self, word):
        """
        Inserts the string word into the Trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create new node if char not found
            node = node.children[char]
        node.is_end = True  # Mark the end of the word

    def search(self, word):
        """
        Returns true if the string word is in the Trie, false otherwise.
        :type word: str
        :rtype: bool
        """
        node = self._find(word)
        return node is not None and node.is_end  # Word must exist and be marked as complete

    def startsWith(self, prefix):
        """
        Returns true if there is a previously inserted string word that has the prefix.
        :type prefix: str
        :rtype: bool
        """
        return self._find(prefix) is not None  # If prefix exists in Trie, return True

    def _find(self, prefix):
        """
        Helper function to traverse the Trie and return the last node of a given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None  # Prefix not found
            node = node.children[char]
        return node  # Return the last node of the prefix

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("apple")
# param_2 = obj.search("apple")
# param_3 = obj.startsWith("app")
