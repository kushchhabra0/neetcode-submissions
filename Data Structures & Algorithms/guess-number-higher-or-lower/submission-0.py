# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo,hi = 0,n+1
        while lo+1 < hi:
            mid = (lo+hi)//2
            if guess(mid) == -1:
                hi = mid
            elif guess(mid) == 1:
                lo = mid
            else:
                return mid
        
        return lo