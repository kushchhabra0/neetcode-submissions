class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []        # Final saare subsets ko store karne ke liye list
        i = 0           # Index pointer jo batayega hum abhi kis element par hain
        subset = []     # Current subset jo hum bana rahe hain
        
        def dfs(i):
            # Base Case: Agar index nums ke len se bada ya barabar ho gaya,
            # matlab humne saare elements ke liye decision le liya hai!
            if i >= len(nums):
                res.append(subset.copy()) # Current subset ki copy bana kar result me daal do
                return                    # Wapas laut jao (backtrack)

            # --- Decision 1: Current element ko subset me SHAMIL KARNA HAI ---
            subset.append(nums[i])        # Element ko subset me daala
            dfs(i + 1)                    # Agle element ke liye recursion call kiya

            # --- Decision 2: Current element ko subset me SHAMIL NAHI KARNA HAI ---
            subset.pop()                  # Jo element abhi daala tha use nikal diya (Backtrack)
            dfs(i + 1)                    # Agle element ke liye bina is number ke call kiya

        # Main function se DFS ko 0th index se shuru kiya
        dfs(i)
        return res