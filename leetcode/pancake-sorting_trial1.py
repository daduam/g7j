class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = []
        for target in range(n, 1, -1):
            i, val = max(enumerate(arr[:target]), key=lambda x: x[1])
            if i + 1 == target:
                continue
            arr = arr[:i+1][::-1] + arr[i+1:]
            ans.append(i+1)
            arr = arr[:target][::-1]
            ans.append(target)
        return ans
