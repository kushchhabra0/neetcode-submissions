class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        pre = suf = 1
        n = len(nums)

        for i in range(n):
            pre *= nums[i]
            suf *= nums[n-1-i]

            res = max(res,pre,suf)

            if pre == 0:
                pre = 1
            if suf == 0:
                suf = 1
        return res           
