class Solution:
    def climbStairs(self, n: int) -> int:
        table = []
        table.append(0) # climbStairs(0) = 0
        table.append(1) # climbStairs(1) = 1 
        table.append(2) # climbStairs(2) = 2
        if n >= len(table):
            for x in range(3, n + 1):
                table.append(table[x - 1] + table[x - 2])
        return table[n]

Test = Solution()
print(Test.climbStairs(5))