import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Characters ki frequency count karo
        count = Counter(s)
        
        # Step 2: Python me default Min-Heap hota hai, isliye hum frequencies ko 
        # negative (-cnt) karke Max-Heap ka behavior achieve karte hain.
        maxHeap = [[-cnt, char] for char, cnt in count.items()] 
        heapq.heapify(maxHeap)

        # 'prev' use hoga us character ko hold karne ke liye jise humne JUST ABHI use kiya hai,
        # taaki wo consecutive places par dubara baith kar string ko invalid na bana de (Cool-down mechanism).
        prev = None
        res = ""
        
        # Jab tak heap me characters hain YA fir koi character cool-down (prev) me baith kar 
        # waapis heap me jaane ka intezar kar raha hai...
        while maxHeap or prev:
            # CRITICAL BOUNDARY CHECK:
            # Agar hamare paas 'prev' me koi character bacha hai, par heap khali ho chuki hai,
            # iska matlab hamare paas use lagane ke liye koi ALTERNATIVE character bacha hi nahi.
            # Aise case me rearrange karna impossible hai -> Return ""
            if prev and not maxHeap:
                return ""
            
            # Heap se sabse HIGH FREQUENCY wala element nikalo (jo 'prev' nahi hai)
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # Kyunki count negative tha, toh use 1 unit consume karne par hum +1 karenge

            # Agar pichla koi character cool-down me bacha tha, toh ab wo safe hai!
            # Use wapis heap me push kar do taaki aage ke scheduling me wo participate kar sake.
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None  # Cool-down clear
                
            # Agar aaj use kiye hue character ki frequency abhi bhi bachi hui hai (< 0),
            # toh use directly heap me mat daalo (warna loop me fir se wahi pop ho jayega).
            # Ise 'prev' me daal kar 1 step ke liye lock kar do.
            if cnt < 0:
                prev = [cnt, char]
        
        return res