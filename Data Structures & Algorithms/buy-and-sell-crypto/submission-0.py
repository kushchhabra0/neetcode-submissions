class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0    # Left pointer track karega sabse sasti BUYING price
        res = 0  # Maximum profit store karega

        # Right pointer se SELLING price check karna shuru karenge (Day 1 se)
        for r in range(1, len(prices)):

            # Case 1: Agar aaj ki price buying price se zyada hai, matlab profit ho raha hai!
            if prices[r] > prices[l]:
                # Max profit ko update karo
                res = max(res, prices[r] - prices[l])
            
            # Case 2: Agar aaj stock aur bhi sasta mil raha hai, toh isi ko naya buying day bana lo
            else:
                l = r # Left pointer ko utha kar right par le aaye
                
        return res