from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Cyclic Sort - Har number ko uski sahi index (num - 1) par swap karo
        for i in range(n):
            # Conditions for swap:
            # 1. Number 1 se n ke beech mein hona chahiye (1 <= nums[i] <= n)
            # 2. Number pehle se apni sahi jagah par nahi hai (nums[i] != nums[nums[i] - 1])
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                # Correct index calculate karo jahan is element ko jana chahiye
                correct_idx = nums[i] - 1
                # Swap elements
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # Step 2: Swap hone ke baad check karo kaunsa index mismatch ho raha hai
        for i in range(n):
            # Agar index i par 'i + 1' nahi milta, toh wahi pehla missing positive hai
            if nums[i] != i + 1:
                return i + 1
                
        # Step 3: Agar 1 se n tak saare elements present hain, toh missing number n + 1 hoga
        return n + 1