# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge Case: Agar list empty ho, single node ho, ya k = 0 rotations hon
        if not head or not head.next or k == 0:
            return head

        # Step 1: List ki length (n) aur last node (tail) find karo
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # Step 2: Unnecessary full rotations eliminate karne ke liye modulo operation
        k %= n
        if k == 0:
            return head  # Agar effective rotations 0 hain, original head return karo

        # Step 3: Linked list ko temporarily circular bana do
        tail.next = head

        # Step 4: Naya tail locate karo jo (n - k)th node (1-based) par hoga
        steps = n - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        # Step 5: Naya head assign karo aur circle ko break karo
        new_head = new_tail.next
        new_tail.next = None

        return new_head