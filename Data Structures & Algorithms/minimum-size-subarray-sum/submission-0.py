class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        l,r,total = 0,0,0
        res = float("inf")

        n = len(nums)
        while r<n:
            total += nums[r]
            while total >= target:
                res = min(r-l+1,res)
                total -= nums[l]
                l += 1
            r +=1
        
        if res == float("inf"):
            return 0    
        return res

        