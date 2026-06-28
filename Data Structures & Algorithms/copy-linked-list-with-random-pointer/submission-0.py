"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # {Old_Node: New_Clone_Node} ka mapping map.
        # None: None handle karega jab kisi node ka next ya random pointer Null ho.
        oldToCopy = {None: None}

        # Step 1: Pehle pass me sirf saare cloned nodes banao aur map me register karo
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next

        # Step 2: Dusre pass me map se unke respective links (next aur random) connect karo
        cur = head
        while cur:
            copy = oldToCopy[cur]
            # Pointers ko map ke zariye safely naye cloned nodes par point karwao
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        # Original head ka cloned head map se utha kar return kar do
        return oldToCopy[head]

        #  A -> A_copy -> B -> B_copy -> None then split and return