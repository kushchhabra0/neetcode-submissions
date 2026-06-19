# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Step 1: Inorder ke elements aur unke indices ka ek HashMap banao
        # Isse hum kisi bhi root ka index O(1) time me dhoond sakte hain
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # Preorder pointer track karega ki hum abhi kaunse root par hain
        self.pre_idx = 0

        # Helper function jo current subtree ki inorder range [in_left, in_right] par kaam karega
        def helper(l, r):
            # Base Case: Agar left pointer right se aage nikal gaya, matlab subtree khali hai
            if l > r:
                return None

            # Preorder se current root ki value uthao aur pointer ko aage badhao
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            # HashMap se is root ka inorder index O(1) me nikalo
            mid = inorder_map[root_val]

            # RECURSION: Left aur Right subtrees ko unki limited boundary ke sath build karo
            # Left subtree ki range: l se lekar mid - 1 tak
            root.left = helper(l, mid - 1)
            
            # Right subtree ki range: mid + 1 se lekar r tak
            root.right = helper(mid + 1, r)

            return root

        # Shuruat me poore inorder array ki range pass karo: [0, len(inorder)-1]
        return helper(0, len(inorder) - 1)