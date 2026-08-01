class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        maxCnt = max(self.cnt.values())
        i = len(self.stack) - 1
        while self.cnt[self.stack[i]] != maxCnt:
            i -= 1
        self.cnt[self.stack[i]] -= 1
        return self.stack.pop(i)