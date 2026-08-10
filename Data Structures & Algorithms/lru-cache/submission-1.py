class Node:
    # Standard Parameter Order: (key, val)
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Map: key -> Node reference
        
        # Dummy nodes for boundary handling:
        # self.left = Least Recently Used (LRU) dummy head
        # self.right = Most Recently Used (MRU) dummy tail
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        # Connect dummy nodes together
        self.left.next = self.right
        self.right.prev = self.left

    # Helper 1: Doubly Linked List se node ko O(1) mein detach karo
    def remove(self, node: Node) -> None:
        prev_node = node.prev
        nxt_node = node.next
        prev_node.next = nxt_node
        nxt_node.prev = prev_node

    # Helper 2: Node ko Doubly Linked List ke MRU end (right dummy ke pehle) insert karo
    def insert(self, node: Node) -> None:
        prev_node = self.right.prev
        nxt_node = self.right
        
        prev_node.next = node
        nxt_node.prev = node
        node.prev = prev_node
        node.next = nxt_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Item access hua: Move to MRU position (Remove & Insert)
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Agar key pehle se present hai, toh purana node detach kar do
            self.remove(self.cache[key])
            
        # Naya Node create karo (Fixed Argument Order: key, value)
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)  # Naye node ko MRU position par daalo

        # Capacity overflow check: LRU element (left.next) ko evict karo
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)          # Remove node from DLL
            del self.cache[lru.key]   # Delete entry from Hash Map