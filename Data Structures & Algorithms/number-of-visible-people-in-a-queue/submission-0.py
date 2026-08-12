from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        st = []  # Monotonic Decreasing Stack stores indices

        for i, v in enumerate(heights):
            # Case 1: Stack mein jitne bhi log current person 'v' se chhote hain,
            # unke right mein pehla bada ya equal person 'v' hi hai.
            # Pop operational step: 'v' in sabhi ko visible hoga, toh unka count +1 badhao.
            while st and heights[st[-1]] <= v:
                res[st.pop()] += 1
            
            # Case 2: Agar stack mein abhi bhi koi index bacha hai, 
            # toh woh person current person 'v' se strictly bada hai.
            # Woh person bhi current person 'v' ko dekh sakta hai (uske aage waale log chhote the, blocked nahi).
            if st:
                res[st[-1]] += 1
            
            # Current person index ko stack mein push karo
            st.append(i)
            
        return res