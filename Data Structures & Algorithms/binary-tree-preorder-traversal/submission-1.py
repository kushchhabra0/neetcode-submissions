class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []
        
        while cur or stack:
            if cur:
                # 1. ROOT: Sabse pehle current node ki value ko result me daalo
                res.append(cur.val)
                
                # Current node ko stack me push karo taaki right subtree par baad me ja sakein
                stack.append(cur)
                
                # 2. LEFT: Left subtree ko pehle priority do aur aage badho
                cur = cur.left
            else:
                # Agar left side khatam ho gayi, toh stack se pichla parent nikalo
                cur = stack.pop()
                
                # 3. RIGHT: Ab us parent ke right child par jao
                cur = cur.right
                
        # Isme koi res.reverse() karne ki zaroorat nahi hai, answer direct milta hai!
        return res