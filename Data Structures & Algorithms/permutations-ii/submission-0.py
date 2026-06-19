class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)
        count = {num:0 for num in nums}
        for num in nums:
            count[num] +=1

        def backtrack():
            if len(perm) == n:
                res.append(perm.copy())
                return

            for num in count:
                if count[num] > 0:
                    perm.append(num)
                    count[num] -=1

                    backtrack()
                    count[num] +=1
                    perm.pop()

        backtrack()
        return res            

