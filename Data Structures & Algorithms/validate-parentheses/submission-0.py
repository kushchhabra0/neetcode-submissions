class Solution:
    def isValid(self, s: str) -> bool:
        # Stack use karenge takki brackets ka nesting aur order perfect check ho sake
        stack = []
        
        # Hash Map / Dictionary jo closing bracket ko uske sahi opening partner se map karti hai
        closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for c in s:
            # Check karo: Kya naya character ek CLOSING bracket hai?
            if c in closeToOpen:
                # Agar closing bracket mila, toh check karo:
                # 1. Stack khali nahi hona chahiye (stack -> True)
                # 2. Stack ka top-most element exactly is closing bracket ka opening partner hona chahiye
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop() # Match mil gaya! Purane opening partner ko stack se uda do
                else:
                    # Agar stack khali hai ya partner match nahi hua, matlab invalid nesting hai
                    return False
            else:
                # Agar character closing nahi hai (yaani opening bracket '[', '{', '(' hai),
                # toh use chupchaap stack me push kar do
                stack.append(c)    
        
        # Aakhir me agar stack poori tarah khali ho gaya (True if not stack), matlab saare pairs valid the.
        # Agar stack me abhi bhi kuch bacha hai, matlab invalid hai (False).
        #return True if not stack else False

        # Aap direct yeh likh sakte hain:
        return not stack