# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # BASE CASE: Jab hum dhoondte-dhoondte kisi 'None' spot (khali jagah) par pahunch jayein,
        # toh iska matlab hume naya node lagane ka sahi adda mil gaya hai.
        # Naya TreeNode banao aur use upar wale parent se link karne ke liye return kar do.
        if not root:
            return TreeNode(val)
        
        # RECURSIVE STEP 1: Agar insert karne wali value current node se badi hai,
        # toh rule ke mutabik hum right subtree me dhoondenge aur naye sub-tree ka root link karenge.
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
            
        # RECURSIVE STEP 2: Agar value current node se choti hai,
        # toh hum left subtree me dhoondenge aur left pointer ko update karenge.
        else:
            root.left = self.insertIntoBST(root.left, val)
            
        # Poore processed aur modified tree ka main root return kar do
        return root