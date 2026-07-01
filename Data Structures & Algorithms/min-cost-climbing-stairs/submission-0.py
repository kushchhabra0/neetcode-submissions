class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10,15,20,0]
        cost.append(0)
        for i in range(len(cost)-3,-1,-1): # start form 15 i.e. second last cost
            
            # take min cost from single jump and double jump

           # cost[i] = min(cost[i]+cost[i+1],cost[i]+cost[i+2])

            # cost[i] is redundant as it common among them so we 
            # can just add it in orignal value
            cost[i] += min(cost[i+1],cost[i+2])
        
        # return the min of starting point cost
        return min(cost[0],cost[1])