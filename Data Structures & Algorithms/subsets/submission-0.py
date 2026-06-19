class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        i = 0
        subset = []
        def dfs(i):
            if i>= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(i)
        return res    

