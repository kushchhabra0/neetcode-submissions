# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        # Bottom-Up DFS (Postorder: Left -> Right -> Root)
        def dfs(node):
            if not node:
                return None
            
            # 1. Pehle extreme niche jao aur bacho ko recursively process/delete karo.
            # Parent ka left aur right pointer unke naye updated status ko catch karega.
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            
            # 2. Ab upar aate waqt (Postorder step), check karo ki kya current node 
            # ek leaf node hai AUR uski value target ke barabar hai?
            # (Agar iske bache niche saaf ho chuke honge, toh node.left aur node.right automatic None ban chuke hain!)
            if node.val == target and not node.left and not node.right:
                # Agar yeh condition true hai, toh is node ko uda do (None return karke parent ko signal do)
                return None
                
            # Agar delete nahi karna hai, toh current healthy node ko as-is return karo
            return node
            
        return dfs(root)