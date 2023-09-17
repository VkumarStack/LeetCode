class Solution:
    def numDecodings(self, s):
        memo = {}
        return self.numDecodingsRec(s, memo)
    def numDecodingsRec(self, s, memo):
        if s in memo:
            return memo[s]
        if len(s) == 0:
            return 0
        # Reach a length 1 string - check if it is a valid int
        if len(s) == 1:
            if int(s) > 0 and int(s) <= 26:
                memo[s] = 1
                return 1
            else:
                memo[s] = 0
                return 0
        # Regardless, if the string starts with 0 it is invalid 
        if s[0] == '0':
            memo[s] = 0
            return 0
        # Length 2 case XX: check if XX is valid and check if X X is valid
        if len(s) == 2:
            memo[s] = 0
            if int(s) > 0 and int(s) <= 26:
                memo[s] = 1
            memo[s] = memo[s] + self.numDecodingsRec(s[1:], memo)
            return memo[s]
        memo[s] = self.numDecodingsRec(s[1:], memo)
        if (int(s[0:2]) > 0 and int(s[0:2]) <= 26):
            memo[s] = memo[s] + self.numDecodingsRec(s[2:], memo)
        else:
            memo[s[2:]] = 0
        memo[s] = self.numDecodingsRec(s[1:], memo) + self.numDecodingsRec(s[2:], memo)
        return memo[s]

test = Solution()
print(test.numDecodings("123123"))