class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # No intervals, simply append
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        
        for i, interval in enumerate(intervals):
            mer = self.merge(interval, newInterval)
            # First case, newInterval can be inserted behind interval without 
            # needing to merge (they are disjoint). 
            if (not mer[0]) and (interval[0] > newInterval[1]):
                intervals.insert(i, newInterval)
                return intervals
            # Second case, newInterval overlaps with interval. In this case,
            # they should be merged but also all intervals after should be 
            # merged if necessary.
            if mer[0]:
                intervals[i] = mer[1]
                while i + 1 < len(intervals):
                    mer = self.merge(intervals[i + 1], intervals[i])
                    if not mer[0]:
                        break
                    intervals[i] = mer[1]
                    intervals.pop(i + 1)
                return intervals
        
        # If the end is reached, then the new interval is to be inserted at the end
        if intervals[-1][1] >= newInterval[0]:
            if newInterval[1] > intervals[-1][1]:
                intervals[-1] = [intervals[-1][0], newInterval[1]]
            return intervals
        intervals.append(newInterval)
        return intervals

    def merge(self, interval1, interval2):
        # Disjointed intervals:
        if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
            return (False, None)
        # Interval 1 is fully inside Interval 2:
        if interval1[0] >= interval2[0] and interval1[1] <= interval2[1]:
            return (True, interval2)
        # Interval 2 is fully inside Interval 1:
        if interval2[0] >= interval1[0] and interval2[1] <= interval1[1]:
            return (True, interval1)
        # Overlap but not fully inside:
        if interval2[1] >= interval1[1]: # Interval 1 to the left of Interval 2
            return (True, [interval1[0], interval2[1]])
        return (True, [interval2[0], interval1[1]]) # Interval 2 to the left of Interval 1

test = Solution()
print(test.insert([[1,2],[5, 6], [7, 8]], [4,9]))


