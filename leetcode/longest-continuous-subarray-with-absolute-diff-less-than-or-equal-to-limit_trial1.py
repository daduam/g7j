class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        incr = deque()
        decr = deque()
        ans, left = 0, 0
        for right in range(len(nums)):
            while incr and nums[right] > incr[-1]:
                incr.pop()
            incr.append(nums[right])
            while decr and nums[right] < decr[-1]:
                decr.pop()
            decr.append(nums[right])
            while incr[0] - decr[0] > limit:
                if nums[left] == incr[0]:
                    incr.popleft()
                if nums[left] == decr[0]:
                    decr.popleft()
                left += 1
            ans = max(ans, right - left + 1)
        return ans