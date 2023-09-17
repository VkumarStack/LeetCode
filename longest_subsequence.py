from cgitb import text
from operator import itemgetter

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # For the longer of the two strings, map the character to the index,
        # allowing for whether it is a valid substring to be checked
        ref = text1 if len(text1) > len(text2) else text2
        sml = text2 if len(text1) > len(text2) else text1
        
        refMap = {}
        for n, ch in reversed(list(enumerate(ref))):
            if ch in refMap:
                refMap[ch].append(n)
            else:
                refMap[ch] = [n]
        
        dp = []
        for n, ch in reversed(list(enumerate(sml))):
            candidates = {}
            if ch not in refMap:
                dp.insert(0, (0, -1))
                continue

            idxs = refMap[ch]
            candidates[idxs[0]] = 1
            
            for item in dp:
                if item[0] == 0:
                    continue
                threshold = item[1]
                for idx in idxs:
                    if idx < threshold:
                        if idx in candidates:
                            candidates[idx] = max(candidates[idx], 1 + item[0])
                        else:
                            candidates[idx] = 1 + item[0]
                        break
            
            highest = max(candidates, key=candidates.get)
            dp.insert(0, (candidates[highest], highest))
        
        return max(dp, key=itemgetter(0))[0]
            



test = Solution()
print(test.longestCommonSubsequence("abcde", "ace"))