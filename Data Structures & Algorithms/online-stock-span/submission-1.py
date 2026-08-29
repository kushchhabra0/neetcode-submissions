class StockSpanner:

    def __init__(self):
        # Monotonic stack jo pairs store karega: (price, us price ka calculated span)
        # Yeh stack hamesha strictly decreasing order (bade se chote) me rahega.
        self.stack = [] 

    def next(self, price: int) -> int:
        # Har naya din apne aap me kam se kam 1 span toh hold karta hi hai
        span = 1
        
        # Jab tak stack khali nahi hai AUR stack ke top par baithe pichle din ki price 
        # aaj ki price se choti ya barabar (<=) hai...
        while self.stack and self.stack[-1][0] <= price:
            # Pichle din ka span aaj ke span me accumulate (add) kar lo
            span += self.stack[-1][1]
            # Us purane element ko pop karke uda do kyunki aaj ka bada price ab uski jagah le lega
            self.stack.pop()
            
        # Aaj ki price aur uske total accumulated span ka pair stack me push karo
        self.stack.append((price, span))

        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)