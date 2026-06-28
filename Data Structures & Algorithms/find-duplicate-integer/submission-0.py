class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Milte hain cycle ke andar kahin par
        # Pehla step manually bahar le liya taaki 'while slow != fast' condition lag sake
        slow = nums[0]
        fast = nums[nums[0]]
        
        # Jab tak slow aur fast aapas mein takra nahi jaate
        while slow != fast:
            slow = nums[slow]          # Ek kadam aage
            fast = nums[nums[fast]]    # Do kadam aage
            
        # Phase 2: Cycle ka entry point (Duplicate) dhoondna
        # Ek naya variable banane ke bajaye fast ko hi utha kar start (0) par patak diya!
        fast = 0
        
        # Ab dono ko strictly ek-ek kadam aage badhao
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        # Jahan dono mile, wahi hamara target duplicate number hai!
        return slow