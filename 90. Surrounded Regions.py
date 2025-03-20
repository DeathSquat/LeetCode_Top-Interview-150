class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Base case: If out of bounds or not 'O', return
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the cell as visited by changing 'O' to 'T' (temporary mark)
            board[r][c] = 'T'
            
            # Explore all four directions (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        
        # Step 1: Capture 'O's on the border and mark them as 'T'
        for r in range(rows):
            for c in [0, cols - 1]:  # Only check first and last column
                if board[r][c] == 'O':
                    dfs(r, c)
        
        for c in range(cols):
            for r in [0, rows - 1]:  # Only check first and last row
                if board[r][c] == 'O':
                    dfs(r, c)

        # Step 2: Flip all 'O's to 'X' and all 'T's back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':  # Surrounded regions
                    board[r][c] = 'X'
                elif board[r][c] == 'T':  # Border-connected regions
                    board[r][c] = 'O'
