class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = n*2
        ans = [1]*l
        i = 0
        while i<n:
            ans[i] = nums[i]
            ans[i+n] = nums[i]
            i+=1
        return ans     