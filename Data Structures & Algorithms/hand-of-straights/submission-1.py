class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Edge Case: Agar total cards groupSize se divide nahi ho rahe, 
        # toh equal partitions banana mathematically impossible hai.
        if len(hand) % groupSize:
            return False
        
        # Step 1: Har card ki frequency (occurrence count) store karne ke liye map banaya
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # Step 2: Unique cards ki list ko Min-Heap mein badal diya
        # Isse hamein hamesha sabse chota available card O(1) mein top par milega
        minH = list(count.keys())
        heapq.heapify(minH)

        # Step 3: Jab tak heap khaali nahi hota, tab tak groups banate jao
        while minH:
            # Heap ke top par jo element hai, wo hamare current group ka starting node hoga
            first = minH[0]

            # Sequence Check: Starting node se lekar 'groupSize' tak ke lagatar numbers dhoondo
            for i in range(first, first + groupSize):
                # Comparison 1: Agar beech ka koi consecutive card count map mein hai hi nahi,
                # toh valid straight hand banana impossible hai, return False!
                if i not in count:
                    return False
                
                # Agar card hai, toh use group mein shamil karke uski frequency 1 ghatao
                count[i] -= 1
                
                # Agar us card ki frequency poori tarah se 0 (khatam) ho chuki hai
                if count[i] == 0:
                    # Smart Optimization: Agar frequency 0 hui hai par wo number abhi heap ke 
                    # top par nahi baitha (yaani usse chote numbers abhi heap mein bache hain), 
                    # toh continuous flow toot jayega. Return False immediately!
                    if minH[0] != i:
                        return False
                    
                    # Agar wo heap ke top par hi hai, toh use heap se safely pop (remove) kar do
                    heapq.heappop(minH)
        
        # Agar saare checks bina kisi failure ke paar ho gaye, toh card collection valid hai
        return True