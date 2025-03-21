class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # If the starting cell or the ending cell is an obstacle, no path exists
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        
        # Create a DP table initialized to 0
        dp = [[0] * n for _ in range(m)]
        
        # Initialize the starting position
        dp[0][0] = 1
        
        # Fill the DP table
        for i in range(m):
            for j in range(n):
                # If there's an obstacle at the current cell, skip it
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] += dp[i-1][j]
                    if j > 0:
                        dp[i][j] += dp[i][j-1]
        
        # The bottom-right corner contains the answer
        return dp[m-1][n-1]
