# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Ek Dummy node banaya aur uske 'next' ko head par point kar diya.
        # Dummy node isliye zaroori hai taaki agar list ka pehla (Head) node hi delete karna pad jaye,
        # toh hamara code crash na kare aur hum aaram se dummy.next return kar sakein.
        dummy = ListNode(0, head)
        
        # Left pointer ko dummy par set kiya aur Right pointer ko actual head par
        left = dummy
        right = head

        # Right pointer ko 'n' steps aage badhao.
        # Isse Left aur Right pointers ke beech me exact 'n' nodes ka gap ban jayega.
        while n > 0:
            right = right.next
            n -= 1

        # Ab dono pointers ko 1-1 step aage badhao jab tak Right pointer 'None' (end) tak nahi pahunch jata.
        # Kyunki dono ke beech me 'n' ka gap tha, jab Right end par pahunchega, 
        # toh Left pointer delete hone wale node ke EKTUM PEHLE (Previous Node) khada hoga!
        while right:
            left = left.next
            right = right.next

        # Link badlo: Left ke agle node ko skip karke uske bhi agle node se jod do.
        # Isse beech wala (Nth from end) node list se bahar (delete) ho jayega.
        left.next = left.next.next
        
        # Actual head return karo jo dummy ke next me safe hai
        return dummy.next  