class MyQueue:

    def __init__(self):
        # s1 ko hum sirf push/input lene ke liye use karenge
        self.s1 = []
        # s2 ko hum sirf pop/peek/output karne ke liye use karenge
        self.s2 = []

    def push(self, x: int) -> None:
        # Standard Queue behavior: Naye element ko hamesha s1 (input stack) me daalo. It's O(1)!
        self.s1.append(x)

    def _move_s1_to_s2(self) -> None:
        # HELPER FUNCTION: Agar output stack (s2) khali hai, tabhi hum s1 se 
        # saare elements ko pop karke s2 me push karenge.
        # Is double-reversal ki wajah se elements ka order FIFO ban jata hai!
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self) -> int:
        # Pehle data transfer check karo, fir s2 ke top se element nikal lo
        self._move_s1_to_s2()
        return self.s2.pop()

    def peek(self) -> int:
        # Pehle data transfer check karo, fir s2 ka aakhiri element (top) dekh lo
        self._move_s1_to_s2()
        return self.s2[-1]

    def empty(self) -> bool:
        # Queue tabhi khali mani jayegi jab dono stacks me koi element na bacha ho
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()