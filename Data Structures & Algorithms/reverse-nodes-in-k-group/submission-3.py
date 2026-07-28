# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            # 1. K-th node find karo
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            # 2. Group ko reverse karo
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Connections set karo
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
            
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

"""
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        group = 0
        
        # Step 1: Check karo ki kya list mein k elements bache hain
        # 'cur' ko k steps aage badhao
        while cur and group < k:
            cur = cur.next
            group += 1
        
        # Step 2: Agar pure k nodes mil gaye hain
        if group == k:
            # Recursive Call: Agle remaining part of list ko pehle hi reverse karke aao
            # Agle group ka jo naya head hoga, wo hamara 'cur' ban jayega
            cur = self.reverseKGroup(cur, k)
            
            # Current k nodes ko in-place reverse karo aur remaining reversed list (cur) se jodo
            while group > 0:
                tmp = head.next    # Next node ko safe jagah store karo
                head.next = cur    # Current node ke pointer ko reversed part (cur) par point karwao
                cur = head         # 'cur' ko ek step aage badhao (current node ab naya reversed head hai)
                head = tmp         # 'head' ko next unreversed node par shift karo
                group -= 1
                
            head = cur  # Head ko naye reversed group ke start par update kar do
            
        return head

"""