# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string."""
        res = []
        
        # Preorder DFS (Root -> Left -> Right)
        def dfs(node):
            # Agar node None hai, toh hum "null" append karenge taaki 
            # deserialize karte waqt tree ka exact structure (leaf nodes) pata chal sake.
            if not node:
                res.append("null")
                return
            
            # Root ki value ko string me convert karke collect karo
            res.append(str(node.val))
            # Left subtree par jao
            dfs(node.left)
            # Right subtree par jao
            dfs(node.right)
        
        dfs(root)
        # Saare collected strings ko comma (,) se join karke ek single string banao
        return ",".join(res) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        # SMART TRICK: String ko comma se split karke uska ek Iterator bana liya.
        # Python Iterator me 'next()' use karne se hume O(1) me agla element milta hai,
        # aur list.pop(0) ki tarah baaki elements shift nahi karne padte (O(N) bachta hai).
        res = iter(data.split(','))
        
        def dfs():
            # Iterator se agli value nikalo
            val = next(res)
            
            # Agar value "null" hai, matlab yahan koi node nahi hai. Return None.
            if val == "null":
                return None
            
            # Agar valid value hai, toh naya TreeNode banao
            node = TreeNode(int(val))
            
            # Preorder fashion me hi pehle left child link hoga, fir right child
            node.left = dfs()
            node.right = dfs()
            
            # Poora structured node return kar do
            return node
        
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))