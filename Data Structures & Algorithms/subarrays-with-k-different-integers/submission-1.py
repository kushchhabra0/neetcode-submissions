from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        
        left_far = 0
        left_near = 0
        ans = 0
        
        for right in range(len(nums)):
            # Step 1: Right element ko frequency map mein add karo
            freq[nums[right]] += 1
            
            # Step 2: Agar unique elements K se zyada ho gaye, window ko shrink karo
            if len(freq) > k:
                del freq[nums[left_near]]
                left_near += 1
                left_far = left_near
            
            # Step 3: Duplicate elements ko left_near se clean karo
            # (Jab tak nums[left_near] ki frequency > 1 hai, use aage badha sakte hain)
            while freq[nums[left_near]] > 1:
                freq[nums[left_near]] -= 1
                left_near += 1
                
            # Step 4: Agar exactly K unique elements hain
            if len(freq) == k:
                # Valid subarrays = left_near se left_far ke beech ki range
                ans += (left_near - left_far + 1)
                
        return ans