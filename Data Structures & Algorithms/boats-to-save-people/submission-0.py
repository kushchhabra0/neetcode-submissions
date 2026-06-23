class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Step 1: Logon ko unke weight ke hisab se sort kar do.
        # Isse halka insaan extreme left par aur bhaari insaan extreme right par aa jayega.
        people.sort()
        
        res = 0  # Yeh total number of boats track karega
        l, r = 0, len(people) - 1  # Left pointer (Halka) aur Right pointer (Bhaari)

        # Jab tak saare log rescue nahi ho jaate
        while l <= r:
            # GREEDY STRATEGY:
            # Sabse bhaari insaan (people[r]) ko boat me baithna hi padega.
            # Hum check karte hain ki use bithane ke baad boat me kitna weight limit 'remain' bacha.
            remain = limit - people[r] 
            r -= 1       # Bhaari insaan safely boat me baith gaya, pointer andar le aao
            res += 1     # Ek boat lag gayi

            # Ab check karo: Kya jo bachi hui capacity hai (remain), usme sabse halka insaan (people[l])
            # bhi baith sakta hai? (l <= r check ensures ki koi bacha bhi ho)
            if l <= r and remain >= people[l]:
                l += 1   # Agar halka insaan fit ho gaya, toh use bhi bitha lo aur pointer aage badhao
        
        return res