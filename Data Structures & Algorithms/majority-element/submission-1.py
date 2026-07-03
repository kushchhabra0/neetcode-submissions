class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = nums[0]
        for i in range(len(nums)):
            if count == 0:
                majority = nums[i]
            if nums[i] == majority:
                count +=1
            else:
                count -=1
        
        return majority