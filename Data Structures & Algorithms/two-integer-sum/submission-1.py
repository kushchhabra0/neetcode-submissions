class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i

        for i in range(len(nums)):    
            diff = target - nums[i]
            if diff in mp and mp[diff] != i:
                return [i,mp[diff]]
        return []        