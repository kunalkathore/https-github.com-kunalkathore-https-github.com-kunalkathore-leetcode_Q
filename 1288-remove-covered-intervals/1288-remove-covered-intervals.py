class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c = len(intervals)
        intervals.sort(key=lambda x: x[0])
        x, y = intervals[0]
        for i in range(1, len(intervals)):
            if x <= intervals[i][0] and intervals[i][1] <= y:
                c -= 1
                continue
            if intervals[i][0] <= x and y <= intervals[i][1]:
                c -= 1
            x, y = intervals[i][0], intervals[i][1]
        return c