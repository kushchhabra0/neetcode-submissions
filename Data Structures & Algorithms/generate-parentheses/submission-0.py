class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [] # Current string ke characters ko track karne ke liye

        def backtrack(openN, closedN):
            # Base Case: Agar open aur closed brackets dono 'n' ke barabar ho gaye,
            # matlab ek valid combination poora ban chuka hai!
            if openN == closedN == n:
                res.append("".join(stack)) # Stack ke chars ko jod kar string banao aur save karo
                return

            # Choice 1: Hum tabhi '(' add kar sakte hain jab uska count 'n' se chota ho
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # Backtrack: Last bracket nikalo taaki choice 2 try ho sake

            # Choice 2: Hum tabhi ')' add kar sakte hain jab uska count 'open' brackets se kam ho
            # Agar closed >= open ho gaya, toh string invalid ban jayegi (jaise "())")
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() # Backtrack: Last bracket nikalo

        # 0 open aur 0 closed brackets se shuruat ki
        backtrack(0, 0)
        return res