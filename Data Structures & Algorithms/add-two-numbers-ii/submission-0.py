from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []

        # Step 1: l1 ke saare values stack s1 mein daalo (MSB -> LSB)
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        
        # Step 2: l2 ke saare values stack s2 mein daalo (MSB -> LSB)
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None

        # Step 3: Stacks se pop karke LSB to MSB addition perform karo
        while s1 or s2 or carry:
            # Stack top se units place digits extract karo
            v1 = s1.pop() if s1 else 0
            v2 = s2.pop() if s2 else 0

            # Sum calculate karo with carry
            total = v1 + v2 + carry
            carry = total // 10
            
            # Step 4: Naya node create karke use list ke front (head) par prepend karo
            node = ListNode(total % 10)
            node.next = head
            head = node  # Naye node ko head bana do
        
        return head