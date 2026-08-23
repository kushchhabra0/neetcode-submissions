class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [] # Isme hum temperatures ke INDICES ko store karenge
        res = [0]*n # Result array ko 0 se initialize kiya (agar koi warmer day na mile toh 0 hi rahega)
        
        for i in range(n):
            curTemp = temperatures[i]

            while stack and curTemp > temperatures[stack[-1]]:
                # 1. Stack se us chote element ka index nikalo
                prev_day_idx = stack.pop()
                
                # 2. Gap nikallo: Aaj ka index minus pichle din ka index
                res[prev_day_idx] = i - prev_day_idx
            # Aaj ke din ka index stack me push kar do (kyunki ab stack ke top par 
            # ya toh isse bada element hai, ya stack khali ho chuka hai)
            stack.append(i)
        
        return res