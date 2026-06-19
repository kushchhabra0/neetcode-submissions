class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Global tracker jo pure tree me se maximum diameter ko store karega
        self.res = 0

        # Helper function: Yeh current node ki 'Height' return karega,
        # par side-by-side global diameter (self.res) ko bhi update karta chalega.
        def dfs(cur):
            # Base Case: Agar node None hai, toh uski height 0 hogi
            if not cur:
                # Leaf node ke niche 0 return hota hai
                return 0
            
            # Left aur Right subtrees ki maximum height nikal lo
            left = dfs(cur.left)
            right = dfs(cur.right)

            # CRITICAL LOGIC (Diameter Calculation): 
            # Is current node se guzarne wala diameter kya hoga? (Left height + Right height)
            # Hum check karte hain kya yeh naya diameter purane max diameter se bada hai?
            self.res = max(self.res, left + right)
            
            # HEIGHT RETURN RULE: 
            # Kisi bhi node ki height hoti hai: 1 (wo node khud) + dono bacho me se jiski height zyada ho
            return 1 + max(left, right)
        
        # Root node se DFS traversal shuru karo
        dfs(root)
        
        # Final maximum diameter return kar do
        return self.res