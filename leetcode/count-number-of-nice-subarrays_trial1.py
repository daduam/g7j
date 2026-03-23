class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        store = []
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                store.append(i)
        ans = 0
        for j in range(len(store) - k + 1):
            if j + k - 1 == len(store) - 1:
                b = (len(nums) - store[j + k - 1])
            else:
                b = abs(store[j + k] - store[j + k - 1])
            if j == 0:
                a = (store[j] + 1)
            else:
                a = abs(store[j - 1] - store[j])
            ans += a * b
        return ans