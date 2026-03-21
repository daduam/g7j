class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        psum = [0] * (n+1)
        for first, last, seats in bookings:
            psum[first-1] += seats
            psum[last] -= seats
        ans = []
        runsum = psum[0]
        for i in range(n):
            ans.append(runsum)
            runsum +=  psum[i+1]
        return ans
        