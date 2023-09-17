class Solution:
    def pacificAtlantic(self, heights):
        memo = {}
        pacific = []
        visited = [[False] * len(heights[0])] * len(heights)
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                self.pacifics(heights, r, c, memo, pacific, visited)
        
        memo = {}
        atlantic = []
        visited = [[False] * len(heights[0])] * len(heights)
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                self.atlantics(heights, r, c, memo, atlantic, visited)
        print(atlantic)

    def pacifics(self, heights, r, c, memo, results, visited):
        visited[r][c] = True

        if (r, c) in memo:
            return memo[(r, c)]
        
        if (r == 0 or c == 0):
            results.append([r, c])
            memo[(r, c)] = True
            return True 
        
        if (r - 1 >= 0) and ((not visited[r - 1][c]) or memo.get((r - 1, c), False)) and (heights[r][c] >= heights[r - 1][c]):
            if self.pacifics(heights, r - 1, c, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 

        if (r + 1 < len(heights)) and ((not visited[r + 1][c]) or memo.get((r + 1, c), False)) and (heights[r][c] >= heights[r + 1][c]):
            if self.pacifics(heights, r + 1, c, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 

        if (c - 1 >= 0) and ((not visited[r][c - 1]) or memo.get((r, c - 1), False)) and (heights[r][c] >= heights[r][c - 1]):
            if self.pacifics(heights, r, c - 1, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 

        if (c + 1 < len(heights[0])) and ((not visited[r][c + 1]) or memo.get((r, c + 1), False)) and (heights[r][c] >= heights[r][c + 1]):
            if self.pacifics(heights, r, c + 1, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 
        
        memo[(r, c)] = False
        return False

    def atlantics(self, heights, r, c, memo, results, visited):
        visited[r][c] = True

        if (r, c) in memo:
            return memo[(r, c)]
        
        if (r == (len(heights) - 1)) or (c == (len(heights[0]) - 1)):
            results.append([r, c])
            memo[(r, c)] = True
            return True 
        
        if (r - 1 >= 0) and ((not visited[r - 1][c]) or memo.get((r - 1, c), False)) and (heights[r][c] >= heights[r - 1][c]):
            if self.atlantics(heights, r - 1, c, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 

        if (r + 1 < len(heights)) and ((not visited[r + 1][c]) or memo.get((r + 1, c), False)) and (heights[r][c] >= heights[r + 1][c]):
            if self.atlantics(heights, r + 1, c, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 

        if (c - 1 >= 0) and ((not visited[r][c - 1]) or memo.get((r, c - 1), False)) and (heights[r][c] >= heights[r][c - 1]):
            if self.atlantics(heights, r, c - 1, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 

        if (c + 1 < len(heights[0])) and ((not visited[r][c + 1]) or memo.get((r, c + 1), False)) and (heights[r][c] >= heights[r][c + 1]):
            if self.atlantics(heights, r, c + 1, memo, results, visited):
                results.append([r, c])
                memo[(r, c)] = True 
                return True 
        
        memo[(r, c)] = False
        return False

test = Solution()
print(test.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
