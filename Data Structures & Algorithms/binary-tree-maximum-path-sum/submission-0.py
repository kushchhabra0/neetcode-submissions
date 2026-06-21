class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global variable jo pure tree me mila ab tak ka absolute maximum path sum track karega.
        # Shuruat me ise root.val se initialize kiya taaki negative values bhi handle ho sakein.
        self.res = root.val
        
        def dfs(node):
            if not node:
                return 0    
            
            # 1. Recursively left aur right subtrees ka max path sum nikalo.
            # CRITICAL OPTIMIZATION: Agar subtree se negative sum aa raha hai, 
            # toh use lene ka koi fayda nahi (chori me nuksaan kyu uthana?), use 0 se max kar do.
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)

            # 2. SPLIT PATH CHECK (Current node ko Apex/Root banakar path complete karna):
            # Kya left child -> current node -> right child wala path ab tak ka best path hai?
            # Is value ko hum global 'self.res' ke sath compare karke update kar dete hain.
            self.res = max(self.res, node.val + leftMax + rightMax)

            # 3. (Return Statement):
            # Kyunki hum upar parent node ke paas laut rahe hain, hum ya toh left branch chun sakte hain ya right.
            # Hum dono branches ek sath parent ko nahi bhej sakte (wo split path ban jayega).
            # Isliye node.val me dono me se jo maximum branch ho use add karke return karo.
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return self.res