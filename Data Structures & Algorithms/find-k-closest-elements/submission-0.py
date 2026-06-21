class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Hum binary search pure array par nahi chalayenge.
        # Hum binary search sirf hamari K-length ki window ke STARTING POINT 'l' par chalayenge.
        # Kyunki window ka size 'k' fixed hai, toh starting point maximum 'len(arr) - k' tak hi ja sakta hai.
        l, r = 0, len(arr) - k

        while l < r:
            mid = (l + r) // 2
            
            # CRITICAL LOGIC (The Window Comparison):
            # Hum check kar rahe hain ki kya 'mid' par khada element window ke aage aane wale 
            # element 'mid + k' ke muqable 'x' ke zyada paas hai ya door?
            #
            # Agar 'x - arr[mid] > arr[mid + k] - x' hai, iska matlab 'x' right side wale element 
            # (arr[mid + k]) ke zyada paas hai. Toh hamari right side wali window better hai!
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1  # Window ko right side me shift karo
            else:
                r = mid      # 'mid' ya uske left wali window better hai ya barabar hai
        
        # Binary search khatam hone ke baad 'l' par hamari perfect window ka starting index hoga.
        # Wahin se lekar agle 'k' elements slice karke return kar do.
        return arr[l : l + k]