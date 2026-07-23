class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum =0
        count = 0
        mp={0:1}
        for num in nums:
            prefixSum +=num

            if (prefixSum -k) in mp:
                count += mp[prefixSum-k]
            
            mp[prefixSum] = mp.get(prefixSum,0)+1
        return count 