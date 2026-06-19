class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # Current window ke characters ki frequency track karne ke liye
        res = 0    # Sabse badi valid window ki length store karega
        l = 0      # Left pointer (Window ki shuruat)

        # Right pointer array ke har character par aage badhega
        for r in range(len(s)):
            # Right side se naya character window me add kiya aur count badhaya
            count[s[r]] = 1 + count.get(s[r], 0)

            # CORE LOGIC: (Current Window Size) - (Most Frequent Character Count)
            # Yeh batata hai ki window me kitne "alag" characters hain jinhe badalna padega.
            # Agar badalne wale characters 'k' se zyada ho gaye, toh window invalid ho gayi!
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1 # Left character ka count kam karo
                l += 1           # Left pointer ko aage badha kar window choti karo

            # Valid window milte hi maximum length ko update karo
            res = max(res, r - l + 1)
            
        return res