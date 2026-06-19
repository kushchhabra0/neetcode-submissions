class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # Saare valid combinations ko store karne ke liye final list

        # Backtrack function jo current 'start' number aur ab tak ka 'comb' (combination) track karega
        def backtrack(start, comb):
            # Base Case: Agar hamare combination ki length 'k' ke barabar ho gayi,
            # matlab hume ek valid combination mil gaya!
            if len(comb) == k:
                res.append(comb.copy())  # Mast iski copy bana kar result me daal do
                return                   # Wapas laut jao (backtrack)

            # Hum 'start' se lekar 'n' tak ke saare numbers par iterate karenge.
            # 'n+1' isliye likha hai kyunki range me last number exclusive hota hai.
            for i in range(start, n + 1):
                # 1. Action: Current number 'i' ko combination me daalo
                comb.append(i)
                
                # 2. Explore: Agle numbers ke liye recursion call karo (start ko i+1 kar diya)
                # i+1 isliye kiya taaki same number ya pichle numbers dobara na aayein (no duplicates like [1, 1] or [2, 1])
                backtrack(i + 1, comb)
                
                # 3. Backtrack: Wapas aate waqt 'i' ko nikal do taaki loop ke agle number ko try kar sakein
                comb.pop()

        # Main function se backtracking ko start=1 aur khaali list [] se shuru kiya
        backtrack(1, [])
        return res