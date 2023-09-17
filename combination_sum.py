class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        ret = { 0 : [True, 1]}
        self.combinationSumRec(nums, target, ret)
        if ret[target][1] is None:
            return 0
        return ret[target][1]
    def combinationSumRec(self, nums, target, memo):
        if target in memo:
            return memo[target][0]
        found = False
        for num in nums:
            if target - num >= 0:
                if self.combinationSumRec(nums, target - num, memo):
                    found = True
                    if target not in memo:
                        memo[target] = [True, memo[target - num][1]]
                    else:
                        memo[target][1] = memo[target][1] + memo[target - num][1]

        if not found:
            memo[target] = [False, None]
            return False
        else:
            return True
        
test = Solution()
print(test.combinationSum4([1, 5], 6))