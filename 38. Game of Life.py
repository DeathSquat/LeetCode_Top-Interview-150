class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        # Define state transitions:
        # 0 -> 0 (dead -> dead) -> stays 0
        # 1 -> 1 (live -> live) -> stays 1
        # 1 -> 0 (live -> dead) -> mark as 2
        # 0 -> 1 (dead -> live) -> mark as 3
        
        def count_live_neighbors(i, j):
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            live_neighbors = 0
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] == 1 or board[ni][nj] == 2):
                    live_neighbors += 1
            
            return live_neighbors
        
        # Step 1: Apply rules with encoding
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # Mark as dying (1 -> 0)
                else:  # Dead cell
                    if live_neighbors == 3:
                        board[i][j] = 3  # Mark as reviving (0 -> 1)
        
        # Step 2: Convert states to final values
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    board[i][j] = 0  # Dead
                elif board[i][j] == 3:
                    board[i][j] = 1  # Alive
