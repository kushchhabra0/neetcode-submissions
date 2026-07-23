class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        # Array ["leet", "co#de"] -> "4#leet5#co#de"
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            # Strictly digits tak hi scan karo jab tak '#' delimiter na mil jaye
            while s[j] != '#':
                j += 1
                
            # Digits segment (i se j-1) ko length mein parse karo
            length = int(s[i:j])
            
            # Substring slice extract karke result mein append karo
            res.append(s[j + 1 : j + 1 + length])
            
            # Pointer 'i' ko exact substring length ke BAAD jump karwao
            i = j + 1 + length
            
        return res