class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ordering = [(score[i], -i) for i in range(len(score))]
        ordering.sort(reverse=True)
        ans = ["0"] * len(ordering)
        for i in range(len(ordering)):
            ans[-ordering[i][1]] = str(i+1)
        ans[-ordering[0][1]] = "Gold Medal"
        if len(ordering) > 1:
            ans[-ordering[1][1]] = "Silver Medal"
        if len(ordering) > 2:
            ans[-ordering[2][1]] = "Bronze Medal"
        return ans
        