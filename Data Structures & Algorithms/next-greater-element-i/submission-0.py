class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {num:i for i,num in enumerate(nums1)}

        res = [-1]*len(nums1)
        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            #check karenge ki cur no. stack ke top se bara hai -> 
            # if yes toh res me nums1 ke us index pe map kar denge res mein
            while stack and stack[-1] < cur:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        
        return res