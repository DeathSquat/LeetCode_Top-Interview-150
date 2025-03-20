from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        
        # Function to convert a square number to (row, col)
        def get_coordinates(square):
            row = (square - 1) // n
            col = (square - 1) % n
            actual_row = n - 1 - row  # Bottom to top
            actual_col = col if row % 2 == 0 else (n - 1 - col)  # Zig-zag pattern
            return actual_row, actual_col
        
        # BFS setup
        queue = deque([(1, 0)])  # (square number, moves)
        visited = set()
        visited.add(1)
        
        while queue:
            square, moves = queue.popleft()
            
            if square == n * n:
                return moves  # Reached the last square
            
            for next_square in range(square + 1, min(square + 6, n * n) + 1):
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]  # Move to snake/ladder destination
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        
        return -1  # Not possible to reach the last square
