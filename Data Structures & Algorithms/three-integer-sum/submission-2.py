class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # 1. CRITICAL STEP: Array ko sort karna bohot zaroori hai.
        # Isse duplicate elements ek saath aa jaate hain aur Two-Pointer lagana aasan ho jata hai.
        nums.sort()
        n = len(nums)
        
        # i hamara first element hoga jisko hum fix karenge
        for i, num in enumerate(nums):
            # Optimization: Agar fixed number hi 0 se bada ho gaya, toh aage ke saare numbers bhi 0 se bade honge (sorted list h).
            # Teen positive numbers ka sum kabhi 0 nahi ho sakta, isliye loop ko yahin BREAK kar do!
            if num > 0:
                break
                
            # Duplicate se bachne ka tareeqa: Agar current number pichle fixed number jaisa hi hai,
            # toh isko SKIP (continue) kar do, nahi toh same triplets dobara ban jayenge.
            if i > 0 and num == nums[i-1]:
                continue

            # Ab bache hue right side ke array me Two Pointers set karo
            l, r = i + 1, n - 1
            
            while l < r:
                threesum = num + nums[l] + nums[r]
                
                # Case 1: Agar sum 0 se bada hai, matlab sum chota karna padega -> right pointer peeche lao
                if threesum > 0:
                    r -= 1
                # Case 2: Agar sum 0 se chota hai, matlab sum bada karna padega -> left pointer aage badhao
                elif threesum < 0:
                    l += 1
                # Case 3: BINGO! Sum exact 0 mil gaya
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Inner duplicate check: Pointers badhane ke baad, agar naya 'l' pichle 'l' ke jaisa hi hai,
                    # toh use tab tak aage badhao jab tak naya unique element na mil jaye.
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                        
        return res