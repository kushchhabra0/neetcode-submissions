from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP Array Setup: Size (len(s) + 1) ka array banaya
        # dp[i] store karega ki kya index 'i' se lekar string ke end tak 
        # ka portion valid words mein segment ho sakta hai ya nahi.
        dp = [False] * (len(s) + 1)
        
        # Base Case: String ke bilkul end (empty string segment) par pahunchne ka 
        # matlab hai ki piche ki saari segments successfully match ho chuki hain.
        dp[len(s)] = True

        # Piche se loop chalayenge index (len(s) - 1) se lekar 0 tak
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Comparison 1: Check karo ki kya word ka size string ke bache hue area ke andar fit hota hai
                # Comparison 2: Check karo ki kya index 'i' se shuru hone wala slice word 'w' ke barabar hai
                if (i + len(w) <= len(s)) and s[i : i + len(w)] == w:
                    # break ho pa raha hai toh sp = True kardo
                    dp[i] = dp[i + len(w)]
                
                # Optimization Break: Agar is index 'i' se string successfully break ho pa rahi hai,
                # toh is index ke liye baaki bache words ko check karne ki zaroorat nahi hai, loop se bahar niklo.
                if dp[i]:
                    break
            
        # Poora calculation complete hone par dp[0] batayega ki starting se poori string valid hai ya nahi
        return dp[0]