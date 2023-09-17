from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt = [float("inf")] * (amount + 1)
        opt[0] = 0
        for i in range(1, len(opt)):
            args = [opt[(i - coin)] for coin in coins if (i - coin) >= 0]
            if len(args) != 0:
                opt[i] = min(args) + 1
        
        if opt[amount] == float("inf"):
            return -1
        else:
            return opt[amount]

test = Solution()
print(test.coinChange([1], 0))