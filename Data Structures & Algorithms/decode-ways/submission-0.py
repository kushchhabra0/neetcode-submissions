from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        # Base Case: Agar string khaali hai ya pehla character '0' hai
        if not s or s[0] == "0":
            return 0
            
        n = len(s)
        
        # DP Array Initialization: Size (n + 1) ka array banaya
        # dp[i] store karega index 'i' se lekar string ke end tak total kitne ways hain
        dp = [0] * (n + 1)
        
        # Base Cases Setup:
        # dp[n] = 1 -> String ke end par pahunchne ka 1 valid tarika hai (Empty string decoding)
        dp[n] = 1  
        
        # Piche se loop chalayenge index (n-1) se lekar 0 tak
        for i in range(n - 1, -1, -1):
            
            # Choice 1: Single Digit Validation
            if s[i] != "0":
                # Agar character '0' nahi hai, toh yeh single step jump le sakta hai
                dp[i] = dp[i + 1]
                
                # Choice 2: Double Digit Validation
                # Check karo ki kya agla character valid boundary mein hai,
                # aur s[i:i+2] strictly "10" se "26" ke beech ka koi combinations bana raha hai
                if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                    # Agar valid hai, toh double step jump ke ways ko bhi jod do
                    dp[i] += dp[i + 2]
            else:
                # Agar s[i] == "0" hai, toh is index se koi decoding shuru nahi ho sakti.
                # Isiliye dp[i] strictly 0 rahega aur hum agle round par chale jayenge.
                dp[i] = 0
                
        # Poora loop khatam hone par dp[0] mein absolute total ways store ho jayenge
        return dp[0]
