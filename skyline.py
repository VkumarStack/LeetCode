class Solution:
    def getSkyline(self, buildings):
        if len(buildings) == 0:
            return []
        if len(buildings) == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        m = len(buildings) // 2
        l = buildings[:m]
        r = buildings[m:]
        return self.mergeSkylines(self.getSkyline(l), self.getSkyline(r))

    def mergeSkylines(self, line1, line2):
        if len(line1) == 0:
            return line2
        if len(line2) == 0:
            return line1
        res = []
        h1, h2 = 0, 0
        i, j = 0, 0
        while (i < len(line1)) and (j < len(line2)):
            if line1[i][0] < line2[j][0]:
                if line1[i][1] >= h2 and (len(res) == 0 or res[-1][1] != line1[i][1]):
                    res.append(line1[i])
                elif h1 >= h2 and (len(res) == 0 or res[-1][1] != h2):
                    res.append([line1[i][0], h2])
                h1 = line1[i][1]
                i = i + 1
            elif line1[i][0] > line2[j][0]:
                if line2[j][1] >= h1 and (len(res) == 0 or res[-1][1] != line2[j][1]):
                    res.append(line2[j])
                elif h2 >= h1 and (len(res) == 0 or res[-1][1] != h1):
                    res.append([line2[j][0], h1])
                h2 = line2[j][1]
                j = j + 1
            else:
                if line1[i][1] > line2[j][1]:
                    h2 = line2[j][1]
                    j = j + 1
                else:
                    h1 = line1[i][1]
                    i = i + 1
        while (i < len(line1)):
            if (len(res) == 0 or res[-1][1] != line1[i][1]):
                res.append(line1[i])
            i = i + 1
        while (j < len(line2)):
            if (len(res) == 0 or res[-1][1] != line2[j][1]):
                res.append(line2[j])
            j = j + 1
        return res
    
test = Solution()
print(test.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))