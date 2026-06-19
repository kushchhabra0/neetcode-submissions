class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Edge Case: Agar main tree khali hai, toh use valid BST mana jata hai
        if not root:
            return True

        # Helper function jo har node ke liye valid min aur max ki range track karega
        def dfs(node, min_val, max_val) -> bool:
            # Base Case 1: Agar hum dhoondte-dhoondte end tak pahunch gaye (None), 
            # toh ab tak ke saare checks valid the. Return True!
            if not node:
                return True
                
            # CRITICAL LOGIC: Current node ki value range ke andar honi chahiye.
            # val <= min_val (chota ya barabar nahi chalega, kyunki BST me strictly unique elements hote hain)
            # val >= max_val (bada ya barabar bhi nahi chalega)
            if node.val <= min_val or node.val >= max_val:
                return False

            # RECURSION STEP WITH RANGE UPDATES:
            # 1. Left subtree me jate waqt: Minimum wahi rahega, par Maximum value badal kar current node.val ho jayegi.
            # 2. Right subtree me jate waqt: Maximum wahi rahega, par Minimum value badal kar current node.val ho jayegi.
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        
        # Shuruat me Root ke liye range -infinity se +infinity tak open hoti hai
        return dfs(root, float('-inf'), float('inf'))