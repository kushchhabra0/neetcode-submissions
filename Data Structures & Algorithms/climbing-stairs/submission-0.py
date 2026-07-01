class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Cases Setup: Bottom up Approch   
        # index 0 (ground) par rehne ka 1 tarika hai.
        # index 1 (1st step) par pahunchne ka bhi 1 tarika hai.
        one,two = 1,1
        for _ in range(n-1):
            # Simultaneous assignment: 
            # 'one' ko up-to-date sum milega aur 'two' ko pichle state ka 'one' mil jayega
            one,two = one + two,one
            # temp = one
            # one = one + two
            # two = temp
        return one

# =====================================================================
# ⏱️ EXECUTION TRACE & DRY RUN FOR n = 5
# =====================================================================
# Initial State (i = 1):
#   one = 1, two = 1
#
# Loop chalega (n - 1) yani (5 - 1) = 4 baar:
#
# ---------------------------------------------------------------------
# Iteration | Operation                  | New 'one' | New 'two'
# ---------------------------------------------------------------------
# Round 1   | one, two = 1 + 1, 1        | 2         | 1
# Round 2   | one, two = 2 + 1, 2        | 3         | 2
# Round 3   | one, two = 3 + 2, 3        | 5         | 3
# Round 4   | one, two = 5 + 3, 5        | 8         | 5
# ---------------------------------------------------------------------
#
# Loop Termination:
#   4 rounds poore hone ke baad loop break ho jayega.
#
# Final Return:
#   one = 8 return hoga.
