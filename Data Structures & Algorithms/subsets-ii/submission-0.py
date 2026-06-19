class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        subset = []
        i=0
        def backtrack(i):
            if i >= len(nums):
                res.add(tuple(subset.copy()))
                return

            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)

        nums.sort()
        backtrack(0)

        return [list(s) for s in res]           
