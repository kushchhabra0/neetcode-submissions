class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        # 26 size ke arrays banaye (a to z ke liye) maps ki jagah (Fast & Efficient)
        s1_count = [0] * 26
        s2_count = [0] * 26

        # Pehle s1 ki length jitni window dono arrays me fill kar lo
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Agar pehli hi window me match mil gaya
        if s1_count == s2_count: 
            return True

        # Sliding Window Shuru: Window ko 1-1 step aage badhao
        l = 0
        for r in range(len(s1), len(s2)):
            # 1. Right side se naya character window me SHAAMIL karo
            s2_count[ord(s2[r]) - ord('a')] += 1
            
            # 2. Left side se purana character window se BAHAR nikaal do
            s2_count[ord(s2[l]) - ord('a')] -= 1
            l += 1 # Left pointer aage badhao window size maintain rakhne ke liye

            # 3. Check karo kya ab dono ke character counts match ho rahe hain
            if s1_count == s2_count:
                return True

        return False