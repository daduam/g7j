class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans, left, right = 0, 0, len(people) - 1
        people.sort()
        while left <= right:
            ans += 1
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
        return ans
        