class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the word when it ends at this node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word  # Mark end of a word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Build Trie from the words list
        trie = Trie()
        for word in words:
            trie.insert(word)

        self.result = set()
        rows, cols = len(board), len(board[0])

        # DFS helper function
        def dfs(node, r, c):
            char = board[r][c]
            if char not in node.children:
                return  # Stop if the letter is not in Trie

            next_node = node.children[char]
            if next_node.word:
                self.result.add(next_node.word)  # Found a valid word
            
            # Mark as visited
            board[r][c] = "#"

            # Explore 4 possible directions
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in next_node.children:
                    dfs(next_node, nr, nc)

            # Restore the board after DFS
            board[r][c] = char

            # Optimization: Remove the leaf node in Trie to prune search space
            if not next_node.children:
                del node.children[char]

        # Start DFS from each cell
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in trie.root.children:
                    dfs(trie.root, r, c)

        return list(self.result)

# Example Usage:
solution = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(solution.findWords(board, words))  # Output: ["eat", "oath"]
