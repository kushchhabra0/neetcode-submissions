class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # Base Case: Agar start pointer end tak pahunch gaya,
            # matlab ek perfect permutation taiyar hai!
            if start == len(nums):
                res.append(nums.copy()) # nums khud hi badal chuka hai, iski copy le lo
                return

            # Start se lekar end tak ke saare elements ko swap karke try karenge
            for i in range(start, len(nums)):
                # 1. Swap: Current 'start' wale element ko 'i'th element se badal do
                nums[start], nums[i] = nums[i], nums[start]
                
                # 2. Explore: Agle index ke liye recursion call karo
                backtrack(start + 1)
                
                # 3. Backtrack: Wapas aate waqt array ko pehle jaisa (original) kar do
                nums[start], nums[i] = nums[i], nums[start]

        backtrack(0)
        return res