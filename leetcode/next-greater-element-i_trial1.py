class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        num2nextgt = defaultdict(lambda: -1)
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            num2nextgt[nums2[i]] = stack[-1] if stack else -1
            stack.append(nums2[i])
        return [num2nextgt[x] for x in nums1]