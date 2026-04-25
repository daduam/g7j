from bisect import bisect_left

class MyCalendar:

    def __init__(self):
        self.bookings = []        

    def book(self, startTime: int, endTime: int) -> bool:
        pos = bisect_left(self.bookings, (startTime, endTime))

        if pos > 0 and self.bookings[pos-1][1] > startTime:
            return False
        
        if pos < len(self.bookings) and self.bookings[pos][0] < endTime:
            return False
        
        self.bookings.insert(pos, (startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)