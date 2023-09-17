class Solution:
    def longestConsecutive(self, nums):
        mappings = {}
        # O(n) since dictionary access and insertion is O(1)
        for n in nums:
            if n in mappings:
                continue
            mappings[n] = [None, None, False] # Right node, Left node, Visited
            if (n - 1 in mappings):
                mappings[n - 1][1] = n
                mappings[n][0] = n - 1
            if (n + 1 in mappings):
                mappings[n + 1][0] = n
                mappings[n][1] = n + 1

        longest = 0
        # O(n) since each num is visited only once 
        for num in mappings:
            length = 0
            # If the node hasn't already been visited
            if not mappings[num][2]:
                length = length + 1
                mappings[num][2] = True
                # Traverse left
                current = mappings[num][0]
                while current is not None:
                    length = length + 1
                    mappings[current][2] = True
                    current = mappings[current][0]
                # Traverse right
                current = mappings[num][1]
                while current is not None:
                    length = length + 1
                    mappings[current][2] = True
                    current = mappings[current][1]
                longest = max(longest, length)
        
        return longest

test = Solution()
print(test.longestConsecutive( [0,3,7,2,5,8,4,6,0,1]))