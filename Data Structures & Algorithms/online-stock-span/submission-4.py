class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        self.s.append(price)

        index = len(self.s) - 1
        span = 0
        while index >= 0 and self.s[index] <= price:
            span += 1
            index -= 1
        
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)