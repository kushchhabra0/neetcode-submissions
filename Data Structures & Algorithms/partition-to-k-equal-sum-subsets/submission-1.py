class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        
        # Base Case 1: Agar total sum 'k' se perfectly divide nahi hota,
        # toh barabar buckets banana impossible hai.
        if total_sum % k != 0:
            # integer division '//' se target nikal rahe hain safety ke liye
            return False
            
        target = total_sum // k
        
        # CRITICAL OPTIMIZATION 1: Badi values ko pehle check karne ke liye reverse sort karo.
        # Isse 'subsetSum + nums[j] > target' wali condition jaldi hit hogi aur recursion jaldi rukega.
        nums.sort(reverse=True)
        
        # Agar sabse bada element hi target se bada hai, toh partition kabhi nahi ho sakta.
        if nums[0] > target:
            return False
            
        used = [False] * len(nums) # Track karega ki kaunsa number kis subset me chala gaya

        def backtrack(i, k, subsetSum):
            # Base Case 2: Agar k == 0 ho gaya, matlab humne saare k-subsets perfectly dhoond liye!
            if k == 0:
                return True
                
            # Base Case 3: Agar current subset ka sum target ke barabar ho gaya,
            # toh agla subset (k-1) dhoondne ke liye dobara index 0 se shuru karo, subsetSum ko 0 karke.
            if subsetSum == target:
                return backtrack(0, k - 1, 0)
                
            # Har ek element ko subset me daal kar explore karne ka loop
            for j in range(i, len(nums)):
                # CRITICAL CORRECTION: Agar number used hai OR sum target ko cross kar raha hai, toh SKIP karo!
                if used[j] or subsetSum + nums[j] > target:
                    continue
                    
                # 1. Action: Current element ko use karo
                used[j] = True
                
                # 2. Explore: Agle elements ke liye recursion call karo (index j+1 se)
                if backtrack(j + 1, k, subsetSum + nums[j]):
                    return True
                    
                # 3. Backtrack: Agar yeh path fail hua, toh element ko wapas free karo
                used[j] = False
                
                # CRITICAL PRUNING 2: Agar naya subset shuru ho raha tha (subsetSum == 0) aur yeh element 
                # fit nahi baitha, toh iske baad wale kisi bhi element se yeh subset kabhi shuru nahi ho payega.
                if subsetSum == 0:
                    break
                    
                # CRITICAL PRUNING 3: Agar agla element bilkul same value ka hai jise humne abhi abhi 
                # fail hote hue dekha hai, toh use dubara process karne ka koi sense nahi banta. Skip duplicates!
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
                    
            return False
        
        # Pehla subset (k), index 0 se aur initial sum 0 se shuru karo
        return backtrack(0, k, 0)