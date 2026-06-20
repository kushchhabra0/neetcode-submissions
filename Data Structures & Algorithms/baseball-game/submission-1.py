class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # 'record' hamara stack hai jo saare valid scores ko store karega
        record = []

        for op in operations:
            if op == '+':
                # '+': Pichle do valid scores ka sum naya score banega.
                # record[-1] sabse aakhiri element hai, record[-2] uske pehle wala.
                # Bina pop kiye direct add karke push karo, order bilkul safe rahega!
                record.append(record[-1] + record[-2])
                
            elif op == 'D':
                # 'D': Pichle valid score (record[-1]) ko double karo aur stack me daalo.
                record.append(2 * record[-1])
                
            elif op == 'C':
                # 'C': Pichla valid score invalid ho gaya, toh stack se top element uda do.
                record.pop()
                
            else:
                # Agar koi number hai (string format me), toh use integer banakar stack me daalo.
                record.append(int(op))
                
        # Aakhir me stack me bache saare scores ka sum return kar do
        return sum(record)