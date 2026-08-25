class TimeMap:

    def __init__(self):
        self.store = {} # key:string, val = [list of [val,timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:

        values = self.store.get(key,[])

        # Invariant Bounds Setup
        lo, hi = -1, len(values)

        while lo + 1 < hi:
            mid = (lo + hi) // 2
            
            # Maximization Invariant Boundary Control:
            # Agar mid ka timestamp target se CHOTA YA BARABAR (<=) hai, toh yeh ek valid candidate hai.
            # 'lo = mid' karke hum ise safe zone me hold rakhte hain aur aage bade timestamps check karte hain.
            if values[mid][1] <= timestamp:
                lo = mid
            else:
                hi = mid
        
        # Agar lo abhi bhi -1 hai, iska matlab koi bhi timestamp target se chota ya barabar mila hi nahi.
        # Agar lo > -1 hai, toh values[lo][0] hi hamara exact maximum valid value hai.
        return values[lo][0] if lo != -1 else ""
