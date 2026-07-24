class Solution:
    def decodeString(self, s: str) -> str:
        string_st = []  # Stack for storing previous partial strings
        count_st = []   # Stack for storing repeat multipliers (k)
        res = ""        # Current decoded string accumulator
        k = 0           # Current multiplier accumulator

        for c in s:
            # Case 1: Multi-digit Number Parser
            if c.isdigit():
                k = k * 10 + int(c)  # Handles multi-digit numbers like "100[a]"
                
            # Case 2: Opening Bracket '[' -> Save State & Reset
            elif c == '[':
                string_st.append(res)  # Freeze outer string state
                count_st.append(k)     # Save repetition count for this bracket scope
                res = ""               # Reset string builder for inner scope
                k = 0                  # Reset number builder
                
            # Case 3: Closing Bracket ']' -> Restore State & Multiply Substring
            elif c == ']':
                temp = res                  # Inner bracket evaluated substring
                res = string_st.pop()       # Restore outer string prefix
                count = count_st.pop()      # Pop multiplier for current scope
                res = res + temp * count    # Append multiplied inner substring to restored prefix
                
            # Case 4: Standard Alphabet Character
            else:
                res = res + c  # Accumulate current scope string

        return res