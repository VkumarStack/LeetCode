class Solution:
    def topKFrequent(self, nums, k):
        # Iterate and map each number to its frequency - O(n)
        mappings = {}
        for num in nums:
            if num in mappings:
                mappings[num] = mappings[num] + 1
            else:
                mappings[num] = 1

        # Sort the mapping by its key value - O(nlogn)
        keys = sorted(mappings, key=mappings.get, reverse=True)
        topK = []
        for i in range(k):
            topK.append(keys[i])
        return topK

        # Complexity: O(n + nlogn) => O(nlogn)


test = Solution()
print(test.topKFrequent([1], 1))