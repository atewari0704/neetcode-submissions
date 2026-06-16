class StockSpanner:
    def __init__(self):
        self.stack = [] # (val,span) better than using 2 stacks        

    def next(self, price: int) -> int:
        span = 1 #refers to what will be the cur price's span

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append( (price,span) )

        return span













        # self.stack.append(price)
        # self.length += 1

        # span = 0

        # for i in range(self.length - 1,-1,-1):
        #     if self.stack[i] <= price:
        #         span += 1
        #     else:
        #         break
        
        # return span 

        # so this essentially add this price to the list
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)