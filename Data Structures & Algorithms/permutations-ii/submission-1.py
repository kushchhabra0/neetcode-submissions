class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        n = len(nums)
        
        # Hash Map banaya jo har unique number ki frequency (count) store karega
        count = {num: 0 for num in nums}
        for num in nums:
            count[num] += 1

        def backtrack():
            # Base Case: Agar current permutation ki length total numbers ke barabar hai
            if len(perm) == n:
                res.append(perm.copy()) # Valid unique permutation mil gaya, copy safe karo
                return

            # Array ke bajaye Hash Map ke unique keys par loop chalaya (Avoids Duplicates)
            for num in count:
                if count[num] > 0:
                    # 1. Action: Number ko use kiya aur frequency kam ki
                    perm.append(num)
                    count[num] -= 1

                    # 2. Explore: Agle slot ke liye recursion call
                    backtrack()
                    
                    # 3. Backtrack: Wapas aate waqt frequency badhayi aur number nikala
                    count[num] += 1
                    perm.pop()

        backtrack()
        return res