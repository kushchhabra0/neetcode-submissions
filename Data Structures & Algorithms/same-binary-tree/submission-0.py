# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Agar dono None hain toh True
        if not p and not q: return True
        # Agar koi ek None reh gaya ya values alag hain toh False
        if not p or not q or p.val != q.val: return False
        
        # Baki recursion will handle
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)