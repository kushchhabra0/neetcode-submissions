class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_sum = sum(matchsticks)
        length = total_sum // 4
        sides = [0] * 4

        # Base Case 1: Agar total sum 4 se perfectly divide nahi hota, 
        # toh square banna namumkin hai!
        if total_sum / 4 != length:
            return False
        
        # Optimization 1: Badi matchsticks ko pehle process karo. 
        # Agar koi badi stick target 'length' se badi hai, toh loop jaldi fail ho jayega.
        matchsticks.sort(reverse=True)

        def backtrack(i):
            # Agar saari matchsticks use ho gayin, matlab square ban gaya!
            if i == len(matchsticks):
                return True

            for j in range(4):
                # Check karo kya current side me yeh stick fit baith rahi hai
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]  # Choose
                    
                    if backtrack(i + 1):        # Explore
                        return True
                        
                    sides[j] -= matchsticks[i]  # Backtrack
                    
            return False
        
        return backtrack(0)