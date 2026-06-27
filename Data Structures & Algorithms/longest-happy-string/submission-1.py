import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        
        # Max-Heap tayaar karo. Strictly wahi characters daalo jinka count > 0 hai.
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count < 0:  # Safer check than just 'if count'
                heapq.heappush(maxHeap, (count, char))
                
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            
            # Check karo: Kya pichle do characters same hain aur aaj bhi wahi aa raha hai?
            if len(res) > 1 and res[-1] == res[-2] == char:
                # Agar koi doosra choice bacha hi nahi hai, toh yahin rukna padega bhaiya!
                if not maxHeap:
                    break
                
                # Doosra sabse zyada frequency wala character nikalo
                count2, char2 = heapq.heappop(maxHeap)
                
                # Use string mein lagao aur uska count ek kam karo (+1 kyunki negative heap hai)
                res += char2
                count2 += 1
                
                # Agar doosra character abhi bhi bacha hai, toh wapas heap mein daalo
                if count2 < 0:
                    heapq.heappush(maxHeap, (count2, char2))
                    
                # Brahmastra Move: Pehla character (char) jise humne is turn mein use NAHI kiya,
                # use bina kisi change ke wapas heap mein push karo aur loop ke agle round par jao!
                heapq.heappush(maxHeap, (count, char))
                
            else:
                # Normal Case: Koi violation nahi hai, bindass sabse bada character use karo
                res += char
                count += 1  # Reduce frequency (closer to 0)
                
                # Agar abhi bhi bacha hai, toh wapas heap mein daalo
                if count < 0:
                    heapq.heappush(maxHeap, (count, char))
                    
        return res