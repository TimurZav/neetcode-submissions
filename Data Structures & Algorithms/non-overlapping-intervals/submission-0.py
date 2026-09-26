class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = []
        counter = 0
        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        for interval in sorted_intervals:
            if result and interval[0] >= result[-1][1]:
                result.append(interval)
            elif result:
                counter += 1
            else:
                result.append(interval)
        return counter