class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n, ans, curlen = len(arr), 1, 1
        for i in range(n-1):
            if (i&1 == 1 and arr[i] > arr[i+1]) or (i&1 == 0 and arr[i] < arr[i+1]):
                curlen += 1
                ans = max(ans, curlen)
            else:
                curlen = 1
        curlen = 1
        for i in range(n-1):
            if (i&1 == 1 and arr[i] < arr[i+1]) or (i&1 == 0 and arr[i] > arr[i+1]):
                curlen += 1
                ans = max(ans, curlen)
            else:
                curlen = 1
        return ans
