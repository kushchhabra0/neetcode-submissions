class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int) # incoming - otgoing == n-1

        # Step 1: Trust relationships ko process karo
        for src,des in trust:
            # Jo banda trust kar raha hai (Outgoing), uska score kam karo
            delta[src] -=1
            # Jis bande par trust kiya ja raha hai (Incoming), uska score badhao
            delta[des] +=1
        
        # Step 2: Check karo ki kya koi aisa banda hai jiska score exactly n - 1 hai
        for i in range(1,n+1):
            if delta[i] == n-1:
                return i
        return -1