class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        
        # Iterative loop jab tak current node valid ho YA stack me elements bache hon
        while cur or stack:
            if cur:
                # 1. ROOT: Current value ko result me daalo
                res.append(cur.val)
                # Current node ko stack me push karo taaki baad me iska Left subtree check kar sakein
                stack.append(cur)
                # 2. RIGHT: Pehle poore right side ko explore karo (This is the trick!)
                cur = cur.right
            else:
                # Agar right khatam ho gaya, toh stack se pichla parent nikalo
                cur = stack.pop()
                # 3. LEFT: Ab us parent ke left child par jao
                cur = cur.left
        
        # SMART TRICK EXPLANATION: 
        # Humne 'Root -> Right -> Left' pattern me elements collect kiye hain.
        # Is list ko reverse karne se yeh perfectly 'Left -> Right -> Root' (Postorder) ban jayega!
        res.reverse()
        
        return res