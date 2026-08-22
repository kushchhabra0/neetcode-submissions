class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0

        def isValid(threshold):
            i,cnt = 0,0
            while i < len(nums)-1:
                if abs(nums[i]-nums[i+1]) <= threshold:
                    cnt += 1
                    i += 2
                else:
                    i+=1
                if cnt == p:
                    return True
            return False
        
        nums.sort()
        l,r = -1,nums[-1] - nums[0]+1
        
        while l+1 < r:

            m = (l+r)//2
            if isValid(m):
                r = m
            else:
                l = m
        return r
