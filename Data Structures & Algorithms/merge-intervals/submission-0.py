class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        prev = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i][0] <= prev[1]: #second interval ka start < prev ka end
                prev[1] = max(prev[1],intervals[i][1]) # merge 
            else:
                merged.append(prev) # no merging so directly push in merge array
                prev = intervals[i] # increment prev    

        merged.append(prev)
        return merged        