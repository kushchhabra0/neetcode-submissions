# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # Helper function: Yeh height return karega agar subtree balanced hai,
        # aur agar unbalanced hai, toh turant -1 return kar dega (Signal of Imbalance).
        def dfs(cur):
            # Base Case: Khaali node ki height hamesha 0 hoti hai aur wo balanced hota hai
            if not cur:
                return 0
            
            # 1. LEFT SUBTREE: Left side ki height nikal lo
            left_height = dfs(cur.left)
            # PRUNING: Agar left subtree hi pehle se unbalanced (-1) hai, toh aage mat check karo
            if left_height == -1:
                return -1
                
            # 2. RIGHT SUBTREE: Right side ki height nikal lo
            right_height = dfs(cur.right)
            # PRUNING: Agar right subtree bhi unbalanced (-1) hai, toh wahin se lout jao
            if right_height == -1:
                return -1
            
            # 3. BALANCE CHECK: Agar left aur right ki height ka farq 1 se zyada hai,
            # toh yeh current node unbalanced hai! Wahin se -1 bhej do upar.
            if abs(left_height - right_height) > 1:
                return -1
                
            # HEIGHT RETURN: Agar sab sahi hai, toh standard height return karo: 1 + max(L, R)
            return 1 + max(left_height, right_height)
            
        # Agar dfs se valid height (>= 0) milti hai toh True, agar -1 milta hai toh False
        return dfs(root) != -1