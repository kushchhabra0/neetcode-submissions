# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Brahmastra Dummy Node: Taaki agar 'left == 1' ho, toh head badalne par bhi edge case handle ho jaye
        dummy = ListNode(0, head)
        
        # Pointers initialization
        leftPrev, cur = dummy, head

        # Step 1: leftPrev ko reverse zone ke theek ek kadam pehle tak le jao
        for _ in range(left - 1):
            leftPrev, cur = cur, cur.next

        # Is point par:
        # leftPrev khada hai 'left-1' index par
        # cur khada hai strictly 'left' index par (reverse hone wala pehla node)
        prev = None
        
        # Step 2: Strictly (right - left + 1) nodes ko locally reverse karo
        for _ in range(right - left + 1):
            tmpNext = cur.next  # Agla node safe zone mein rakho
            cur.next = prev     # Link ko ulta ghumao
            prev, cur = cur, tmpNext  # Pointers ko ek-ek kadam aage badhao

        # Step 3: Tute hue connections ko wapas dhasu tarike se jodo!
        # leftPrev.next abhi bhi us node ko point kar raha hai jo pehle 'left' par tha (aur ab reversed sub-list ka tail ban chuka hai).
        # Us tail ke aage bacha hua safe zone list ('cur') jod do.
        leftPrev.next.next = cur
        
        # leftPrev ke next ko ab reversed sub-list ke naye head ('prev') par set kar do.
        leftPrev.next = prev

        # Dummy ka next hi hamara naya aur updated head hoga
        return dummy.next        