class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res,maxHeap = "",[]
        for count,char in [(-a,'a'),(-b,'b'),(-c,'c')]:
            if count:
                heapq.heappush(maxHeap,(count,char))
        
        while maxHeap:
            count,char = heapq.heappop(maxHeap)

            if len(res)>1 and res[-1]==res[-2]==char:
                # agr heap hi khtm ho gyi toh or char kaha se dalenge toh break 
                if not maxHeap:
                    break
                # ek char or pop karna parega same nahi dal sakte
                count2,char2 = heapq.heappop(maxHeap)

                # res me add kar sakte hai ye char ko
                # or count ko kam karna hai us char ke mtlb maxheap hai toh ulta 
                res += char2
                count2 +=1

                # agr abhi bhi char ka count bacha hai toh vapis heap me dal do 
                if count2:
                    heapq.heappush(maxHeap,(count2,char2))
            # normal case 
            else:
                res += char
                count +=1

            # agr abhi bhi char ka count bacha hai toh heap me dal do
            if count:
                heapq.heappush(maxHeap,(count,char))
        
        return res

