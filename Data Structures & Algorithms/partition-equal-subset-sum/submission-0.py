from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # Edge Case Comparison: Agar total sum odd (visham) hai, 
        # toh use do equal integers parts mein divide karna mathematically impossible hai.
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
        # dp set store karega saare unique valid sums ko
        dp = set()
        dp.add(0)
        
        # Piche se loop chalayenge index tracking ke liye
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            
            for t in dp:
                # Comparison & Pruning 1: Aaj ka element jodne par agar sum 
                # strictly target se chota ya barabar hai, tabhi use set mein jagah do!
                if t + nums[i] <= target:
                    nextDP.add(t + nums[i])
                
                # Purana sum toh hamesha safe hai hi (Kyunki humne element nahi uthaya)
                nextDP.add(t)
                
            # Early Termination: Agar target naye set mein generate ho chuka hai,
            # toh aage ke elements ko scan karne ka koi faida nahi, kissa yahin khatam karo!
            if target in nextDP:
                return True
                
            dp = nextDP
            
        return target in dp