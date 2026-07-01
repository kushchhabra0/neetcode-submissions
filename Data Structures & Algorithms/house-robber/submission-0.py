class Solution:
    def rob(self, nums: List[int]) -> int:
        # this is without any circular wall constraint
        # like nums[-1] and nums [0] can be robbed simultaneously
        rob1,rob2 = 0,0
        for num in nums:
            rob1,rob2 = rob2,max(num+rob1,rob2)
        
        return rob2