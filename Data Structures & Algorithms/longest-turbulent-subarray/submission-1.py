from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return n
            
        l = 0
        r = 1
        res = 1
        prev = ""  # Track karega pichla direction: ">", "<", ya ""
        
        while r < n:
            # Condition 1: Decreasing Trend (arr[r-1] > arr[r])
            if arr[r - 1] > arr[r]:
                if prev != ">":
                    res = max(res, r - l + 1)
                    prev = ">"
                    r += 1
                else:
                    # Pattern toot gaya (Dobara '>' aa gaya)
                    # Nayi window pichle element (r-1) se shuru hogi
                    l = r - 1
                    prev = ""  # Reset direction so that current transition is re-evaluated
                    
            # Condition 2: Increasing Trend (arr[r-1] < arr[r])
            elif arr[r - 1] < arr[r]:
                if prev != "<":
                    res = max(res, r - l + 1)
                    prev = "<"
                    r += 1
                else:
                    # Pattern toot gaya (Dobara '<' aa gaya)
                    # Nayi window pichle element (r-1) se shuru hogi
                    l = r - 1
                    prev = ""  # Reset direction
                    
            # Condition 3: Equal Elements (arr[r-1] == arr[r])
            else:
                # Equal elements turbulence chain ko poori tarah tod dete hain
                # Nayi window current element 'r' se hi shuru hogi
                r += 1
                l = r - 1
                prev = ""
                
        return res