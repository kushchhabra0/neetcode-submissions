# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        # Helper function jo har node ke liye ek pair return karega:
        # [Max money if we ROB this node, Max money if we SKIP this node]
        def dfs(node):
            # Base Case: Agar ghar khali hai (None), toh lootne par bhi 0 aur skip par bhi 0 milega.
            if not node:
                return [0, 0]

            # Left aur Right subtrees (padosi gharon) se unke options mangwao
            leftPair = dfs(node.left)
            rightPair = dfs(node.right)

            # OPTION 1: ROB CURRENT NODE (Ghar me chori karo)
            # Rule ke mutabik agar humne current node ko loota, toh hum iske immediate bacho 
            # (leftPair[0] aur rightPair[0]) ko touch BHI nahi kar sakte! 
            # Hume chupchaap unke 'skip' wale amounts (index 1) ko uthana padega.
            withroot = node.val + leftPair[1] + rightPair[1]
            
            # OPTION 2: SKIP CURRENT NODE (Ghar ko chhod do)
            # Agar hum current node ko chhod rahe hain, toh humare paas azaadi hai!
            # Hum left subtree se chahe rob wala amount uthaein ya skip wala (jo bhi max ho -> max(leftPair))
            # Aur same azaadi right subtree ke liye bhi milegi (max(rightPair)).
            withoutroot = max(leftPair) + max(rightPair)

            # Dono options ko upar wale parent node ke liye return kar do
            return [withroot, withoutroot]

        # Root node se shuru karo aur dono me se jo bhi max value de, wahi hamara final answer hai!
        return max(dfs(root))