class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, index):
            if index == len(word):  # Word is completely found
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"  # Mark as visited
            
            # Explore all four directions
            found = (dfs(r+1, c, index+1) or 
                     dfs(r-1, c, index+1) or 
                     dfs(r, c+1, index+1) or 
                     dfs(r, c-1, index+1))
            
            board[r][c] = temp  # Restore the cell
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
