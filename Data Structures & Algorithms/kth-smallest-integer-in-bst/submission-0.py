# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur, stack = root, []
        n = 0  # Counter jo track karega ki hum ab tak kitne elements pop (visit) kar chuke hain
        
        # Standard Iterative Inorder Traversal Framework
        while cur or stack:
            if cur:
                # Jitna left ja sakte ho jao, kyunki BST me sabse chote elements extreme left me hote hain
                stack.append(cur)
                cur = cur.left
            else:
                # extreme left par pahunchne ke baad, stack se sabse chota node pop karo
                cur = stack.pop()
                
                # Ek node visit ho gaya, toh counter ko 1 se badhao
                n += 1
                
                # CRITICAL MATCH: Agar humne exact 'k' elements visit kar liye hain, 
                # toh yahi current node hamara kth smallest element hai!
                if n == k:
                    return cur.val
                
                # Ab right subtree par jao check karne ke liye
                cur = cur.right