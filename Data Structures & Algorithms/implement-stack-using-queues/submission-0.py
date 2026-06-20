from collections import deque

class MyStack:

    def __init__(self):
        # Stack ko simulate karne ke liye sirf ek standard queue use karenge
        self.q = deque()

    def push(self, x: int) -> None:
        # Step 1: Naye element ko queue ke piche (end me) append karo
        self.q.append(x)
        
        # Step 2: Queue ko rotate karo!
        # Naye element ke aane se pehle jitne bhi elements queue me the (len(q) - 1),
        # un sabko ek-ek karke aage se popleft() karo aur wapas piche append() kar do.
        # Is rotation se jo naya element end me aaya tha, wo automatic queue ke FRONT (head) par aa jayega!
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Kyunki push() ke waqt rotation ne Last-In element ko hamesha FRONT par set kar diya hai,
        # toh pop karne ke liye hume bas standard queue ka popleft() chalana hai. It's O(1)!
        return self.q.popleft()

    def top(self) -> int:
        # Queue ka sabse pehla element (index 0) hi stack ka TOP element ban chuka hai. It's O(1)!
        return self.q[0]

    def empty(self) -> bool:
        # Check karo kya queue khali hai
        return len(self.q) == 0
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()