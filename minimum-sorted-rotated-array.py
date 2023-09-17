class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
        
        left = 0
        right = len(nums) - 1
        while (left != right and right - left != 1):
            midLeft = left + (right - left) // 2
            midRight = left + (right - left + 1) // 2

            if (nums[midLeft] < nums[left]):
                right = midLeft
            elif (nums[right] < nums[midRight]):
                left = midRight
            else:
                if midLeft == midRight:
                    if nums[right] < nums[left]:
                        left = midRight
                    else:
                        right = midLeft
                else:
                    if nums[midLeft] < nums[midRight]:
                        right = midLeft
                    elif nums[midRight] < nums[midLeft]:
                        left = midRight
                    else:
                        if nums[left] > nums[right]:
                            left = midRight
                        else:
                            right = midLeft
        
        return min(nums[left], nums[right])

test = Solution()
print(test.findMin([10,1,10,10,10]))