from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, n):
        # Har account ko shuruat mein uska apna parent/leader banaya
        self.par = [i for i in range(n)]
        # Size/Rank array initialize kiya 1 se (har set ka initial size 1 hai)
        self.rank = [1] * n

    def find(self, x):
        # Path Compression: Root parent dhoondte waqt pointers ko direct grand-parent par point kar do
        # Isse tree height flatten ho jaati hai aur subsequent lookups O(1) ke paas ho jaate hain
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]  # Path halving / Compression
            x = self.par[x]
        return x
    
    def union(self, x1, x2):
        # Dono indices ke root leaders dhoondo
        p1, p2 = self.find(x1), self.find(x2)
        
        # Agar dono pehle se hi same set/component ka part hain, toh union ki zaroorat nahi
        if p1 == p2:
            return False
            
        # Union by Rank/Size: Chote tree ko hamesha bade tree ke niche attach karo
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
            
        return True 


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        
        # Map: email -> pehli baar kis account index par dekha gaya (email -> int)
        emailToAcc = {} 

        # Step 1: Emails scan karo aur identical emails milne par account indices ko Union karo
        for i, a in enumerate(accounts):
            # a[0] account holder ka name hai, a[1:] saari emails hain
            for e in a[1:]:
                if e in emailToAcc:
                    # Agar yeh email pehle kisi aur account mein aa chuki hai,
                    # toh dono accounts ko DSU mein aapas mein jod (union) do
                    uf.union(i, emailToAcc[e])
                else:
                    # Varna email to index mapping mein insert kar do
                    emailToAcc[e] = i
        
        # Step 2: Sabhi unique emails ko unke absolute Parent (Root Leader) account par group karo
        emailGroup = defaultdict(list) # leader account index -> list of emails

        for e, i in emailToAcc.items():
            # Find operation chalana zaroori hai kyunki union hone se parent change ho sakta hai
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        # Step 3: Combined accounts ko format karo: [Name, sorted_email_1, sorted_email_2, ...]
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]  # Representative account index se name uthao
            res.append([name] + sorted(emails))  # Emails ko lexicographically sort karo
            
        return res