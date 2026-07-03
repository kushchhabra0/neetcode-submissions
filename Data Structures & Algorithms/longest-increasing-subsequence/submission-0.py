class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]*(len(nums)+1) # DP array

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)): # for each num check its right element
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i],1+LIS[j])
        
        return max(LIS)