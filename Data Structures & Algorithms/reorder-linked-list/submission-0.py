# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # ----------------------------------------------------
        # STEP 1: Find the middle of the linked list
        # ----------------------------------------------------
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Ab 'slow' pointer middle node par hai.
        # Iske aage se hamari second list shuru hoti hai.
        second = slow.next
        slow.next = None  # Pehli list ko beech se break kar diya (end ko None kiya)
        
        # ----------------------------------------------------
        # STEP 2: Reverse the second half of the list
        # ----------------------------------------------------
        prev = None
        curr = second
        while curr:
            nxt = curr.next   # Agla node save kiya
            curr.next = prev  # Pointer ulta ghumaya
            prev = curr       # prev ko aage badhaya
            curr = nxt        # curr ko aage badhaya
            
        # Ab 'prev' hamari reversed second list ka head ban chuka hai
        second = prev 
        
        # ----------------------------------------------------
        # STEP 3: Merge both halves alternately (Zigzag merge)
        # ----------------------------------------------------
        first = head  # Pehli list ka pointer
        
        while second:
            # Dono lists ke agle nodes ko save kar lete hain taaki link na toote
            tmp1 = first.next
            tmp2 = second.next
            
            # Connection lagao: First ke baad Second, fir Second ke baad purana First.next
            first.next = second
            second.next = tmp1
            
            # Pointers ko agle nodes par bhej do execution chalaye rakhne ke liye
            first = tmp1
            second = tmp2