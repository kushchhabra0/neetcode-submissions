class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # Window ke unique characters ko store karne ke liye
        left = 0        # Left pointer (Window ki shuruat)
        maxLen = 0         # Longest substring ki maximum length track karega

        # Right pointer string ke har character par aage badhega
        for right in range(len(s)):
            # Agar right wala character pehle se set me hai (Duplicate Found!)
            # Toh left se tab tak characters remove karo jab tak duplicate hat na jaye
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1 # Left pointer aage badha kar window choti ki
            
            # Naya unique character set me daalo
            charSet.add(s[right])
            
            # Maximum length ko update karo (Current window size = right - left + 1)
            maxLen = max(maxLen, right - left + 1)    
            
        return maxLen