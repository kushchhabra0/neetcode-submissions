class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = x
        for i in range(n-1):
            res = (res+1) | x
        return res