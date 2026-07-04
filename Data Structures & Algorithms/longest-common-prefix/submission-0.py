from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge Case: Agar input list khaali hai, toh common prefix empty string hoga
        if not strs:
            return ""
            
        # Outer loop strictly pehli string ke characters ki length tak chalega (e.g., 0 se 5 tak 'flower' ke liye)
        for i in range(len(strs[0])):
            # Inner loop baaki saari strings par iterate karega character match karne ke liye
            for s in strs:
                # Comparison 1: Check karo ki kya current string 's' khatam toh nahi ho gayi (out of bounds)
                # Comparison 2: Check karo ki kya current string ka character pehli string ke character se alag hai
                if i == len(s) or s[i] != strs[0][i]:
                    # Agar dono mein se kuch bhi sach hua, toh index 'i' se pehle tak ka slice hi prefix hai
                    return s[:i]
                    
        # Agar poora loop bina kisi mismatch ke khatam ho gaya, 
        # iska matlab pehli string khud hi sabse choti aur poori common prefix hai
        return strs[0]