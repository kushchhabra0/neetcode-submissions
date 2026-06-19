class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        for ch in s:
            mp[ch] = mp.get(ch,0) +1

        for ch in t:
            if ch not in mp or mp[ch] == 0:
                return False
            mp[ch] -= 1 # reduce the count of checked chars

        return True

      

