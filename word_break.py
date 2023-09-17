class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict.sort()
        memo = {}
        return self.wordBreakRec(s, wordDict, memo)

    def wordBreakRec(self, s: str, wordDict: list[str], memo) -> bool:
        if s in memo:
            return memo[s]
        if s == '':
            return True
        
        found = False
        for word in wordDict:
            if len(s) >= len(word) and s[0:len(word)] == word:
                found = self.wordBreakRec('' if len(s) == len(word) else s[len(word):len(s)], wordDict, memo)
                if found:
                    return True
        
        memo[s] = found
        return found

                


test = Solution()
print(test.wordBreak("aaaaaaa", ["aaaa","aaa"]))

