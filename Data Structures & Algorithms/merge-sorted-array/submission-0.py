from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers initialization strictly from the back
        p1 = m - 1          # Pointer for nums1 valid elements
        p2 = n - 1          # Pointer for nums2 elements
        last = m + n - 1    # Pointer for insertion at the very end of nums1
        
        # Loop tab tak chalega jab tak dono arrays mein elements compare karne ke liye bache hain
        while p1 >= 0 and p2 >= 0:
            # Comparison: Agar nums1 ka current element nums2 se bada hai,
            # toh bada element piche safe space mein jayega aur p1 piche khiske ga.
            if nums1[p1] > nums2[p2]:
                nums1[last] = nums1[p1]
                p1 -= 1
            else:
                # Comparison: Agar nums2 ka element bada ya barabar hai nums1 se,
                # toh nums2 ka element piche jayega aur p2 piche khiske ga.
                nums1[last] = nums2[p2]
                p2 -= 1
            # Har element insert hone ke baad insertion pointer ek kadam left shift hoga
            last -= 1
            
        # Remaining Elements Check:
        # Case 1: Agar nums1 ke elements pehle khatam ho gaye (p1 < 0) par nums2 mein bache hain (p2 >= 0),
        # toh unhe bache hue left slots mein as-is copy karna compulsory hai.
        # Case 2: Agar nums2 ke elements pehle khatam ho gaye (p2 < 0), toh loop chalne ki need nahi hai,
        # kyunki nums1 ke bache hue elements already apni sahi sorted jagah par hi khade hain.
        while p2 >= 0:
            nums1[last] = nums2[p2]
            p2 -= 1
            last -= 1