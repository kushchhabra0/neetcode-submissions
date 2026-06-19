class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # Saare valid combinations ko store karne ke liye list

        # DFS function jo current index 'i', ab tak ka combination 'curr', 
        # aur unka sum 'total' track karega
        def dfs(i, curr, total):
            # Base Case 1: Agar total sum target ke barabar ho gaya!
            if total == target:
                res.append(curr.copy())  # Mast photo (copy) khinch ke result me daal do
                return

            # Base Case 2: Agar index out of bounds ho gaya YA total sum target se bada ho gaya,
            # toh aage check karne ka koi fayda nahi (Dead End)
            if i >= len(candidates) or total > target:
                return

            # --- Decision 1: Current element ko combination me SHAMIL KARNA HAI ---
            curr.append(candidates[i])
            # Kyunki hum ek element ko BAAR-BAAR use kar sakte hain, 
            # isliye humne index ko 'i' hi rakha, use 'i+1' nahi kiya!
            dfs(i, curr, total + candidates[i])

            # --- Decision 2: Current element ko aur use NAHI KARNA HAI (Skip it) ---
            curr.pop()  # Backtrack: Jo element abhi add kiya tha use nikal do
            # Ab hum is element se thak gaye hain, toh agle element par badhte hain (i+1)
            dfs(i + 1, curr, total)

        # Main call: 0th index, khaali list [], aur 0 total sum se shuru kiya
        dfs(0, [], 0)
        return res