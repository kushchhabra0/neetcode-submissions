# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Case: Agar main tree khatam ho gaya (None) aur hume subRoot nahi mila,
        # toh iska matlab subRoot is tree ka hissa nahi hai. Return False!
        if not root:
            return False

        # 1. Check karo kya current node se shuru hone wala tree hi subRoot ke jaisa hai?
        if self.isSameTree(root, subRoot):
            return True

        # 2. Agar current node par match nahi mila, toh subtree ko dhoondo:
        # Main tree ke left child me 'YA' main tree ke right child me. (Isliye 'or' lagaya)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Agar dono None hain toh True
        if not p and not q: return True
        # Agar koi ek None reh gaya ya values alag hain toh False
        if not p or not q or p.val != q.val: return False
        
        # Baki recursion will handle
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)