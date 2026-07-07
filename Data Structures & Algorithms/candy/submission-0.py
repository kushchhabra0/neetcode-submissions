class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]*len(ratings)
        
        # left value check
        for i in range(0,len(ratings)):
            if i >0 and ratings[i-1] < ratings[i] :
                candies[i] = candies[i-1] +1
        
        # right se left check karenge ki koi canie update hui toh neighbor ki bhi max update kar de
        for i in range(len(ratings)-1,-1,-1):

            if i < len(ratings)-1 and ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] +1,candies[i])

        return sum(candies)