class Solution:
    def rob(self, nums):
        if len(nums) <= 2:
            return max(nums)
        memo = {}
        return max(self.robRec(nums, 0, memo), self.robRec(nums, 1, memo))
    def robRec(self, nums, idx, memo):
        if idx in memo:
            return memo[idx]

        money = nums[idx]
        immed = 0
        if idx + 2 < len(nums):
            immed = self.robRec(nums, idx + 2, memo)
        skip = 0 
        if idx + 3 < len(nums):
            skip = self.robRec(nums, idx + 3, memo)    
        money = money + max(immed, skip)
        memo[idx] = money
        return money

test = Solution()
print(test.rob([2, 7, 9, 3, 1]))
        