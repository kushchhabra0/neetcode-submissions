class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum =0
        count = 0
        mp={0:1}
        for i in range(len(nums)):
            prefixSum +=nums[i]

            if (prefixSum -k) in mp:
                count += mp[prefixSum-k]
            
            mp[prefixSum] = mp.get(prefixSum,0)+1
        return count 