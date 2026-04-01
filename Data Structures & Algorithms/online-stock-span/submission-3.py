class StockSpanner:

    # Monotonic decreasing stack
    # Brute force approach iterates backwards, repeatedly scanning
    # every element until one is greater. Using a decreasing stack
    # we store pairs of the price and its span. We pop element prior as long
    # as they are less than or equal, since if its smaller, everything in that
    # elements span will also be smaller, so we can add the span to the current element
    # This way, we avoid rescanning old sequences

    def __init__(self):
        self.stack = [] # pair: (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)