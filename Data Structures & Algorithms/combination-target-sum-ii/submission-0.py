class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # Important: Saare duplicates ek sath lane ke liye
        n = len(candidates)

        def backtrack(i, cur, total):
            # Base Cases
            if total == target:
                res.append(cur.copy()) # Target mil gaya, copy safe karo
                return
            if i == n or total > target:
                return # Dead end (Out of bounds ya sum bada ho gaya)

            # Choice 1: Current element ko INCLUDE karo
            cur.append(candidates[i])
            backtrack(i + 1, cur, total + candidates[i])
            cur.pop() # Backtrack: Element nikalo taaki choice 2 check ho sake

            # Choice 2: Current element ko EXCLUDE karo + duplicates skip karo
            # Agar [1, 2, 2] me pehla '2' choda, toh agla '2' bhi chodna padega
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1 # Pointer aage badhao jab tak naya unique number na aaye
                
            backtrack(i + 1, cur, total) # Naye unique element se call

        backtrack(0, [], 0)
        return res