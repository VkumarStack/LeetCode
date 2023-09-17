class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = 0
        chars = {}
        while right < len(s) and left < len(s):
            if left == right:
                chars[s[right]] = right
                right = right + 1
            elif s[right] in chars and (chars[s[right]] <= right and chars[s[right]] >= left):
                left = chars[s[right]] + 1
                chars[s[left]] = left
            else:
                chars[s[right]] = right
                right = right + 1
            length = max(length, right - left)
        return length
test = Solution()
print(test.lengthOfLongestSubstring("ppwwkewaww"))