class Solution:
    def countSubstrings(self, s: str) -> int:
    
        res = 0
     
        # We are going to check through middle
        # and start expanding right and left -> This is the DP approach 

        for i in range(len(s)):
            # for odd length:
            l,r = i,i
            while l>=0 and r< len(s) and s[l] == s[r]:
                res +=1
                l -=1
                r+=1
            
            # for even length 
            l,r = i,i+1
            while l>=0 and r< len(s) and s[l] == s[r]:
                res +=1
                l -=1
                r+=1
        
        return res
