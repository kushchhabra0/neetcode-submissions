class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Problem constraints ke mutabik location hamesha 0 se 1000 ke beech hoti hai.
        # Isliye hum strictly O(1) space me ek fixed size Difference Array bana lete hain.
        passChange = [0] * 1001

        # Step 1: Har trip ke liye entries Difference Array me mark karo
        for t in trips:
            numPass, start, end = t
            
            # Jab gadi 'start' location par aayegi, passengers badhenge (+numPass)
            passChange[start] += numPass
            
            # Jab gadi 'end' location par pahunchegi, passengers utar jayenge (-numPass)
            # NOTE: Passengers drop-off stop par hi utar rahe hain, isliye usi index par subtraction safe hai.
            passChange[end] -= numPass
        
        currPass = 0
        
        # Step 2: Timeline ke hisab se linear order me move karo aur Prefix Sum nikaalo
        for i in range(1001):
            # Aaj ki location par net kitne passengers badhe ya kam hue, use accumulate karo
            currPass += passChange[i]
            
            # CRITICAL BOUNDARY CHECK:
            # Agar kisi bhi location par total onboard passengers car ki capacity se zyada ho gaye,
            # toh yeh pool schedule impossible hai -> Return False
            if currPass > capacity:
                return False
        
        # Agar poori timeline bina capacity cross kiye guzar gayi, toh ride fully safe hai!
        return True