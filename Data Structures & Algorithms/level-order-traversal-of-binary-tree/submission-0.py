import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        
        # Initial Step: Root node ko queue me dalo (Chahe wo None hi kyun na ho)
        q.append(root)

        # Loop tab tak chalega jab tak queue me elements hain
        while q:
            level = []  # Current level ke nodes ki values store karne ke liye list
            
            # CRITICAL STEP (Snapshot): Loop shuru hone se pehle current queue ka size nikal lo.
            # Yeh 'qLen' batata hai ki is specific level me exact kitne nodes hain.
            # Is loop ke andar naye push hone wale (next level ke) nodes is iteration me disturb nahi karenge.
            qLen = len(q)
            
            for i in range(qLen):
                node = q.popleft() # Queue ke aage se node nikalo
                
                # Agar node valid (not None) hai, toh uski value collect karo aur uske bacho ko push karo
                if node:
                    level.append(node.val)
                    
                    # Next level ke liye bacho ko queue me dalo (dono None ho sakte hain, upar check ho jayega)
                    q.append(node.left)
                    q.append(node.right)
            
            # Agar current level me kuch values collect hui hain, toh use final result me daal do
            if level:
                res.append(level)
        
        return res