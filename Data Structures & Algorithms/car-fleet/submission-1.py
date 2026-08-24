class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Step 1: Position aur Speed ko aapas me pair up karo
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        
        # Step 2: Cars ko unki position ke hisab se REVERSE SORTED order me process karo.
        # Yaani jo car target ke sabse paas hai (sabse aage hai), wo pehle process hogi.
        for p, s in sorted(pair)[::-1]:
            # Target tak pahunchne me is car ko kitna TIME lagega: (target - position) / speed
            arrival_time = (target - p) / s
            stack.append(arrival_time)
            
            # CRITICAL LOGIC (The Fleet Collision):
            # Agar stack me kam se kam 2 cars hain, aur jo naye aane wali piche ki car hai
            # uska time (stack[-1]) aage wali car ke time (stack[-2]) se kam ya barabar (<=) hai,
            # iska matlab piche wali car tez chal rahi thi aur wo aage wali car se TAKRA JAYEGI!
            # Kyunki takraane ke baad wo aage wali ki speed par chalegi, wo dono ek FLEET ban jayengi.
            # Isliye hum piche wali car ko stack se pop() karke uda dete hain (kyunki wo aage wale me merge ho gayi).
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        # Aakhir me stack ka size hi total unique fleets batayega
        return len(stack)