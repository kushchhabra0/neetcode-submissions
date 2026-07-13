from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # 3 independent boolean flags track karenge ki kya hamein 
        # target[0], target[1], aur target[2] ke barabar elements mil chuke hain ya nahi.
        f0 = f1 = f2 = False
        
        for t in triplets:
            # Greedy Filter: Agar triplet ka koi bhi element target se bada hai, 
            # toh use merge karne par hum kabhi target nahi bana paayenge. Isiliye drop it!
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
                
            # Agar triplet safe hai, toh independent positions ko match karo
            if t[0] == target[0]: f0 = True
            if t[1] == target[1]: f1 = True
            if t[2] == target[2]: f2 = True
            
            # Early Termination: Agar teeno target elements mil chuke hain,
            # toh aage ke triplets dekhne ka koi faida nahi, yahin se True return kar do!
            if f0 and f1 and f2:
                return True
                
        # End mein agar teeno flags True hain, toh answer True hoga, varna False
        return f0 and f1 and f2