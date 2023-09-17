# Notes:
# Want the most amount of gas accumulated from the beginning
# This can be done by finding the longest sequence that has a net gain in gas (so gas - cost is > 0) and starting from there.

class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        startIndex = self.findLongestGasGain(gas, cost)
        currentIndex = startIndex
        currentGas = gas[startIndex]
        for i in range(len(gas)):
            currentGas -= cost[currentIndex]
            if currentGas < 0:
                return -1
            if i == len(gas):
                currentIndex = 0
            currentGas += gas[currentIndex]
        
        return startIndex

    def findLongestGasGain(self, gas, cost) -> int:
        bestIndex = -1
        currentIndex = -1
        bestLength = 0
        startBestLength = 0
        for i in range(len(gas)):
            if gas[i] - cost[i] >= 0:
                if currentIndex == -1:
                    currentIndex = i
            elif currentIndex != -1:
                if currentIndex == 0:
                    startBestLength = (i - currentIndex)
                if (i - currentIndex) >= bestLength:
                    bestLength = i - currentIndex
                    bestIndex = currentIndex
                currentIndex = -1
        
        if currentIndex != -1:
            if (len(gas) - currentIndex) + startBestLength >= bestLength:
                bestIndex = currentIndex

        return bestIndex
    
test = Solution()
print(test.findLongestGasGain([5, 6, 1, 10, 10, 0, 1, 7], [3, 1, 4, 5, 2, 2, 1, 1]))