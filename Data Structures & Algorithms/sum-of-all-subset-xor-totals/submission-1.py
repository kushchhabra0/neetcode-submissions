class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        # DFS function jo current index 'i' aur ab tak ka XOR 'total' track karega
        def dfs(i, total):
            # Base Case: Jab saare elements khatam ho jayein (index end tak pahunch jaye)
            # Toh is subset ka jo bhi final XOR total aaya hai, use return kar do
            if i == len(nums):
                return total

            # Har element ke paas firse 2 decisions hain:
            
            # Decision 1: Current element ko XOR total me SHAAMIL KARNA HAI
            # Isliye total ke saath nums[i] ka XOR kiya -> (total ^ nums[i])
            include = dfs(i + 1, total ^ nums[i])

            # Decision 2: Current element ko SHAAMIL NAHI KARNA HAI
            # Isliye total ko bina chede waisa ka waisa hi aage bhej diya -> (total)
            exclude = dfs(i + 1, total)

            # End me dono paths se jo XOR sums mile hain, unhe add (plus) karke return kar do
            return include + exclude  

        # 0th index aur 0 initial XOR total se recursion shuru kiya
        return dfs(0, 0)   