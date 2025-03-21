class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Number of rows and columns in the grid
        m, n = len(grid), len(grid[0])

        # DP table to store the minimum path sum up to each cell
        dp = [[0] * n for _ in range(m)]

        # Initialize the top-left corner with the starting point
        dp[0][0] = grid[0][0]

        # Initialize the first column (can only move down)
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # Initialize the first row (can only move right)
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # Fill the rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

        # The bottom-right corner will have the minimum path sum
        return dp[m-1][n-1]
