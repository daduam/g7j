class StockSpanner:

    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.stack[-1][1] <= price:
            self.stack.pop()[0]
        ans = self.i - self.stack[-1][0] if self.stack else self.i
        self.stack.append((self.i, price))
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)