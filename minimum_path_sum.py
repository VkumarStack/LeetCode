class Solution:
    def minPathSum(self, grid):
        # OPT[m, n] = grid[m][n] + min(OPT[m - 1][n], OPT[m][n - 1])
        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        dp[-1][-1] = grid[-1][-1]
        for i in reversed(range(len(grid))):
            for j in reversed(range(len(grid[0]))):
                if (i + 1 < len(grid)) and (j + 1 < len(grid[0])):
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
                elif (i + 1 < len(grid)):
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                elif (j + 1 < len(grid[0])):
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
        return dp[0][0]

test = Solution()
print(test.minPathSum([[1,2,3],[4,5,6]]))