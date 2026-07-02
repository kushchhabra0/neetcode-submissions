from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP Array Setup: Size (amount + 1) ka array initialize kiya.
        # Default value humne 'amount + 1' rakhi hai (jo ki ek tarah se Infinity ka kaam karegi),
        # kyunki agar hum sirf 1$ ke coins bhi use karein, toh max coins 'amount' hi lag sakte hain.
        # Isliye 'amount + 1' se bada answer kabhi possible hi nahi hai.
        dp = [amount + 1] * (amount + 1)
        
        # Base Case: Amount 0 banane ke liye strictly 0 coins chahiye.
        dp[0] = 0
        
        # Outer Loop: 1 se lekar target amount tak har ek amount ke liye state compute karenge
        for a in range(1, amount + 1):
            # Inner Loop: Har ek available coin ko check karenge
            for c in coins:
                # Boundary Check: Coin tabhi use ho sakta hai jab uski value 
                # hamare current target amount 'a' se choti ya barabar ho
                if a - c >= 0:
                    # State Transition Function:
                    # min(aaj tak ka best way, 1 coin aaj ka + bache hue 'a - c' amount ka best way)
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        # Return Check: Agar target index par abhi bhi default value ('amount + 1') baithi hai,
        # iska matlab un coins se yeh amount banana impossible hai, toh -1 return karo.
        # Agar modify ho gayi hai, toh vahi hamara minimum coins ka answer hai.
        return dp[amount] if dp[amount] != amount + 1 else -1