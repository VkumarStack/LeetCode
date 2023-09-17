class Solution:
    def groupAnagrams(self, strs):
        groups = {}
        # O(mnlogn), where m is the size of each string and n is the length of strs
        for str in strs:
            sortedString = ''.join(sorted(str))
            if sortedString in groups:
                groups[sortedString].append(str)
            else:
                groups[sortedString] = [str]
        return list(groups.values())

test = Solution()
print(test.groupAnagrams(["a"]))