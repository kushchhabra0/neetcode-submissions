class Solution:
    # Helper function: Two-pointer approach se check karega ki substring palindrome hai ya nahi
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []   # Saare valid partitionings ko store karega
        part = []  # Current path/partition ko track karega

        def dfs(i):
            # Base Case: Agar index 'i' string ke end tak pahunch gaya, 
            # matlab humne poori string ka ek valid partition dhoond liya hai!
            if i >= len(s):
                res.append(part.copy()) # Deep copy (.copy()) banana zaroori hai
                return
            
            # Shuruat 'i' se karke har possible end point 'j' tak substring check karo
            for j in range(i, len(s)):
                # Agar s[i...j] ek palindrome hai, toh yeh ek valid cut hai
                if self.isPali(s, i, j):
                    part.append(s[i:j+1]) # 1. Choose: Substring ko current path me daalo
                    dfs(j+1)              # 2. Explore: Agle characters ke liye bacha hua part check karo
                    part.pop()            # 3. Backtrack: Wapas aate waqt ise nikal do
        
        dfs(0) # Index 0 se DFS shuru karo
        return res