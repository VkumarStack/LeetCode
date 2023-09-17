class Solution:
    def canJump(self, nums) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True
        count = nums[0]
        for n in range(1, len(nums)):
            if count >= 1:
                reachable[n] = True
                count = max(count, nums[n])
            else:
                return False
            count = count - 1
        return reachable[len(nums) - 1]

test = Solution()
print(test.canJump(
[3,2,1,0,4]))
