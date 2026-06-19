# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        # Iterative loop: Jab tak current node valid hai, tab tak BST ke hissab se navigate karo
        while cur:
            # CASE 1: Agar 'p' aur 'q' dono ki values current node se badi hain,
            # toh iska matlab LCA pakka right subtree me hoga. Right me mud jao!
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
                
            # CASE 2: Agar 'p' aur 'q' dono ki values current node se choti hain,
            # toh iska matlab LCA pakka left subtree me hoga. Left me mud jao!
            elif p.val < cur.val and q.val < cur.val: 
                cur = cur.left
                
            # CASE 3 (The Split Point / Intersection):
            # Agar ek value choti hai aur dusri badi (ya koi ek khud current node ke barabar hai),
            # toh iska matlab isi point par raste alag ho rahe hain. Yahi current node hamara LCA hai!
            else:
                return cur