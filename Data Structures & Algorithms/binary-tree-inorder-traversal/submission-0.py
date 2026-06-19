class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        
        while cur or stack:
            if cur:
                # 1. LEFT: Pehle value collect NAHI karni hai! 
                # Chupchaap current node ko stack me dalo aur jitna left ja sakte ho jao.
                stack.append(cur)
                cur = cur.left
            else:
                # Agar left side khatam ho gayi (None mil gaya), toh stack se parent nikalo
                cur = stack.pop()
                
                # 2. ROOT: Jab node stack se pop ho raha ho, US WAQT uski value collect karo
                res.append(cur.val)
                
                # 3. RIGHT: Ab us node ke right child par jao
                cur = cur.right
                
        return res