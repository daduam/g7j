class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = []
        start, end = intervals[0]
        for s, e in intervals:
            if s >= start and e <= end:
                continue
            if s > end:
                ans.append([start, end])
                start = s
                end = e
            else:
                end = e
        ans.append([start, end])
        return ans
        