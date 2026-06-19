# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Base Case: Agar tree khali hai ya dhoondte-dhoondte None par aa gaye, toh bas None return karo
        if not root:
            return root
        
        # PHASE 1: TARGET NODE KO DHOONDO (Standard BST Search)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        # PHASE 2: TARGET NODE MIL GAYA (Ab delete karne ka khel shuru)
        else:
            # CASE 1: Node ka koi Left child nahi hai (Ya toh yeh leaf node hai ya sirf right child hai)
            # Toh chupchaap right child ko upar bhej do (Agar leaf hoga toh automatically None upar jayega)
            if not root.left:
                return root.right
                
            # CASE 2: Node ka koi Right child nahi hai (Sirf left child hai)
            # Toh left child ko upar parent se link karne ke liye return kar do
            elif not root.right:
                return root.left

            # CASE 3: Node ke pass DONO bache (Left aur Right) maujood hain!
            # Hum is node ko seedhe delete nahi kar sakte, iski jagah iska 'Inorder Successor' dhoondenge.
            # Inorder Successor = Right subtree ka sabse chota element.
            cur = root.right
            while cur.left:
                cur = cur.left   # Jitna left ja sakte ho jao sabse choti value dhoondne
                
            # Sabse chote node ki actual value ko current root me copy karo
            root.val = cur.val
            
            # Ab right subtree me jao aur us duplicated 'Inorder Successor' node ko wahan se permanently delete kar do
            root.right = self.deleteNode(root.right, root.val)

        return root