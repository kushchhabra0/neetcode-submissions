class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Base Case: Agar target string 't' khali hai, toh koi window ban hi nahi sakti
        if t == "": return ""

        # countT: Target string 't' ke characters ki required frequency track karega
        # window: Current sliding window ke andar ke characters ki frequency track karega
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # 'need' batata hai ki kitne UNIQUE characters ki frequency match karni hai
        # 'have' batata hai ki current window me kitne unique characters ki frequency criteria meet ho chuki hai
        have, need = 0, len(countT)
        
        # res store karega best window ke [left_idx, right_idx] aur resLen uski length track karega
        res, resLen = [-1, -1], float("inf")
        l = 0
        
        # Right pointer se window ko expand karte chalo
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # CRITICAL MATCH CHECK:
            # Agar naya character hamare target me hai, AUR uski current frequency exact 
            # target frequency ke barabar pahunch gayi hai, toh hamara ek criteria meet ho gaya ('have' += 1)
            if c in countT and window[c] == countT[c]:
                have += 1
            
            # SHRINKING PHASE (The While Loop):
            # Jab tak hamari window me saare required characters maujood hain (have == need),
            # tab tak window ko left side se chota karke minimum possible size dhoondne ki koshish karo.
            while have == need:
                # 1. Update our best result if the current window is smaller
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                # 2. Window ke left-most character ko pop/remove karo
                left_char = s[l]
                window[left_char] -= 1
                
                # 3. Agar left-most character target ka part tha aur uske hatne se uski frequency 
                # required frequency se kam ho gayi, toh hamara ek criteria toot gaya ('have' -= 1)
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                
                # Left pointer ko aage badhao window shrink karne ke liye
                l += 1

        # Agar resLen update hui thi, toh indices ka use karke substring slice karo, nahi toh ""
        l, r = res
        return s[l : r + 1] if resLen != float("inf") else ""