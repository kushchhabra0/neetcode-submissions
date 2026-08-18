class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if num hamara start ho skta hai kya
            if (num-1) not in numSet:
                # ya num hamara start hai so hame iske aage ke consecutive elements check karnge and current subsequence ki length calc karenge
                length = 1
                while (num + length) in numSet:
                    length +=1
                
                # now update our longest subsequence
                longest = max(longest,length)
        
        return longest
