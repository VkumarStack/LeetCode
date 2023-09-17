class Solution:
    def numIslands(self, grid):
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    islands = islands + 1
                self.dfs_traverse(grid, r, c)
        return islands

    def dfs_traverse(self, grid, r, c):
        if grid[r][c] == "0" or grid[r][c] == "2":
            return
        grid[r][c] = "2"
        if r + 1 < len(grid):
            self.dfs_traverse(grid, r + 1, c)
        if r - 1 >= 0:
            self.dfs_traverse(grid, r - 1, c)
        if c + 1 < len(grid[0]):
            self.dfs_traverse(grid, r, c + 1)
        if c - 1 >= 0:
            self.dfs_traverse(grid, r, c - 1)

test = Solution()
print(test.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))