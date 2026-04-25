from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sintervals = sorted([(a[0], a[1], i) for i, a in enumerate(intervals)])
        ans = []
        for i in range(len(intervals)):
            start, end = intervals[i]
            found = bisect_left(sintervals, (end, start, i))
            ans.append(-1 if found == len(sintervals) else sintervals[found][2])
        return ans