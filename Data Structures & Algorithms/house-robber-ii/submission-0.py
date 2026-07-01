class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def houseRob1(nums):
            rob1,rob2 = 0,0
            for num in nums:
                rob1,rob2 = rob2,max(num+rob1,rob2)
            return rob2
        
        n = len(nums)
        return max(houseRob1(nums[0:n-1]),houseRob1(nums[1:n]))