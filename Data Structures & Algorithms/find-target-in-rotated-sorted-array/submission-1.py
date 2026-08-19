class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = -1, len(nums)
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
                
            # Check if left half is normally sorted
            if nums[lo + 1] <= nums[mid]:
                if nums[lo + 1] <= target < nums[mid]:
                    hi = mid  # Target is inside left sorted half
                else:
                    lo = mid  # Explore right half
            else:
                # Right half is normally sorted
                if nums[mid] < target <= nums[hi - 1]:
                    lo = mid  # Target is inside right sorted half
                else:
                    hi = mid  # Explore left half
                    
        return -1