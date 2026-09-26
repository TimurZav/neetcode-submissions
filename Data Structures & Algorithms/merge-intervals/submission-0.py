class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        for interval in sorted_intervals:
            if result and result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result