class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        slow = fast = head
        # Pehle 'fast' check karo, fir uske next aur next.next ko
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Ab list ekdum barabar 50-50 hisson me tootegi
        scnd = slow.next
        slow.next = None

        # Second half ko reverse karo
        prev = None
        cur = scnd
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Max twin sum nikal lo
        res = 0
        first = head
        scnd = prev
        while first and scnd:
            twinsum = first.val + scnd.val
            res = max(res, twinsum)
            first = first.next
            scnd = scnd.next

        return res