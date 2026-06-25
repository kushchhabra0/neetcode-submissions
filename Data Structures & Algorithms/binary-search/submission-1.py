class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi = -1,len(nums)

        while lo+1 < hi:
            mid = (lo + hi)//2
            if nums[mid]>target:
                hi = mid
            elif nums[mid]<target:
                lo = mid
            else:
                return mid
            
        
        return -1
