# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # BASE CASE
        # if not head.next.next:
        #     return head.val + head.next.val
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        scnd = slow.next
        slow.next = None

        prev = None
        cur = scnd
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        res = 0
        first = head
        scnd = prev
        while first and scnd:
            twinsum = first.val + scnd.val
            res = max(res,twinsum)
            first = first.next
            scnd = scnd.next

        return res    
