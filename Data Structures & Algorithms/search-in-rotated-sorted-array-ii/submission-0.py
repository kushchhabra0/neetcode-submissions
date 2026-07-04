class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo,hi = -1,len(nums)

        while lo+1<hi:
            mid =  lo + (hi-lo)//2
            if nums[mid] == target:
                return True
            
            if nums[lo+1] < nums[mid]: # target on left sorted half
                if nums[lo+1] <= target < nums[mid]:
                    hi = mid 
                else:
                    lo = mid
            
            elif nums[lo+1] > nums[mid]: # target on right sorted half
                if nums[mid] < target <= nums[hi-1]:
                    lo = mid
                else:
                    hi = mid
            else: # not sure about postion of target(due to duplicates)
                lo +=1
        
        return False
