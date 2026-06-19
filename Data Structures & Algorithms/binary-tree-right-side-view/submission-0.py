import collections

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Edge Case: Agar tree khali hai, toh chupchaap khali list return karo
        if not root:
            return []
            
        res = []
        # Queue me sirf valid nodes hi daalenge (Faltu None push nahi karenge)
        q = collections.deque([root])

        while q:
            qLen = len(q)
            
            # Level-by-level loop chalao
            for i in range(qLen):
                node = q.popleft()
                
                # CRITICAL LOGIC: Agar hum current level ke bilkul AAKHIRI element (i == qLen - 1)
                # par khade hain, toh right side se dekhne par yahi node sabse pehle dikhega!
                # Isko direct result me append kar do.
                if i == qLen - 1:
                    res.append(node.val) # Ab agar value '0' bhi hui, toh koi dikkat nahi hogi!
                
                # Sirf valid bacho ko hi aage queue me push karo
                if node.left:  
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
                    
        return res

        """
        # Left Side View ke liye bas yeh condition badal do:
                if i == 0:
                    res.append(node.val)

    """