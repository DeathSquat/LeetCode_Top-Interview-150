class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Define sets to track seen numbers in rows, columns, and sub-boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):  # Iterate over rows
            for j in range(9):  # Iterate over columns
                num = board[i][j]
                if num == '.':  # Skip empty cells
                    continue
                
                # Calculate box index
                box_index = (i // 3) * 3 + (j // 3)
                
                # Check for duplicates
                if num in rows[i]:
                    return False
                if num in cols[j]:
                    return False
                if num in boxes[box_index]:
                    return False
                
                # Add the number to the respective sets
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
        
        # If no duplicates found, the board is valid
        return True
