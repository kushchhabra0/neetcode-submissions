class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # Edge case: Agar 0 pairs chahiye, toh max difference hamesha 0 hoga
        if p == 0:
            return 0

        # Helper function: Check karo kya hum threshold difference ke sath kam se kam 'p' pairs bana sakte hain?
        def isValid(threshold):
            i, cnt = 0, 0
            while i < len(nums) - 1:
                # Greedy choice: Adjacent elements ka difference threshold ke andar hai toh pair bana lo
                if nums[i + 1] - nums[i] <= threshold:
                    cnt += 1
                    i += 2  # Ek element dobara use nahi ho sakta, isliye 2 step aage badho
                else:
                    i += 1  # Pair nahi bana, agle element se try karo
                
                # Pruning: Jaise hi 'p' pairs ban gaye, turant True return karo
                if cnt == p:
                    return True
            return False
        
        # Step 1: Elements ko sort karo taaki minimum difference hamesha adjacent elements me mile
        nums.sort()
        
        # Invariant Bounds:
        # l = -1 (Impossible difference), r = max possible difference + 1
        l, r = -1, nums[-1] - nums[0] + 1
        
        # Step 2: Binary search on difference answer
        while l + 1 < r:
            m = (l + r) // 2
            if isValid(m):
                r = m  # Valid difference mil gaya, chota difference dhoondo
            else:
                l = m  # Pairs nahi ban paaye, difference badhao
                
        return r