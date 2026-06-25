# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # Boundaries set kari strictly standard framework ke hisab se
        lo, hi = 0, n + 1
        
        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            # Brahmastra: API ko ek hi baar call karo aur result save karo
            res = guess(mid)
            
            if res == 0:
                # Jackpot! Element mil gaya, seedhe return maaro
                return mid
            elif res == -1:
                # mid bada hai target se (guess is higher), yaani target left mein hai
                # Isliye unsafe/higher boundary 'hi' ko piche khiskao
                hi = mid
            else:
                # res == 1, matlab mid chota hai target se (guess is lower), target right mein hai
                # Isliye safe/lower boundary 'lo' ko aage badao
                lo = mid
                
        # Invariant framework ke mutabik agar exact match upar nahi mila (jo ki ideal case mein mil jayega),
        # toh loop tootne par hi ya lo boundary par hi element hoga.
        return lo