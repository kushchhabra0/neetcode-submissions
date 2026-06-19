# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # Helper function: 'node' current element hai aur 'maxVal' ab tak ka path-maximum hai
        def dfs(node, maxVal):
            # Base Case: Agar node None hai, toh yahan se 0 good nodes milenge
            if not node:
                return 0
            
            # CRITICAL CHECK: Agar current node ki value ab tak ke maxVal se badi ya barabar hai,
            # toh yeh ek "Good Node" hai, isliye 'res = 1', nahi toh '0'.
            res = 1 if node.val >= maxVal else 0

            # Agle bacho (left/right) ke liye maxVal ko update karo node ki ASLI value se!
            maxVal = max(node.val, maxVal)
            
            # Left aur Right subtrees me jao aur unke good nodes ko current result me add kar lo
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        # Shuruat me root node khud hamesha good node hota hai, 
        # isliye shuruat ki maxVal me bhi root.val hi pass karenge.
        return dfs(root, root.val)
    