class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = curSum = 0
        for R in range(len(arr)):
            curSum += arr[R]
            if R >= k - 1:
                res += curSum >= threshold
                curSum -= arr[R - k + 1]
        return res