from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP array initialization: dp[a] store karega amount 'a' banane ke total unique ways
        # Base case: Amount 0 banane ka strictly 1 hi tarika hota hai (koi coin mat uthao)
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        # COMBINATION RULE: Outer loop strictly COINS ka hona chahiye.
        # Isse ek coin ke saare possible contributions pure array mein ek hi baar process hote hain,
        # jisse duplicate permutations (like [1,2] and [2,1]) avoid ho jaati hain.
        for c in coins:
            # Inner loop chalega coin ki value se lekar target amount tak
            for a in range(c, amount + 1):
                # Comparison/Update: Aaj ka amount banane ke naye ways = 
                # purane ways (bina is coin ke) + 'amount - c' banane ke ways (is coin ke saath)
                dp[a] += dp[a - c]
                
        return dp[amount]