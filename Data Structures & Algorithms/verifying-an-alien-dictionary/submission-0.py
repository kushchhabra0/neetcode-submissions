from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Alien order ka mapping character se uske index tak
        ordToind = {c: i for i, c in enumerate(order)}

        # Har adjacent pair of words ko compare karenge
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Dono strings mein se jo bhi choti hogi, loop strictly wahan tak chalega
            for j in range(min(len(w1), len(w2))):
                # Target Check: Pehla mismatch character dhoondo
                if w1[j] != w2[j]:
                    # Comparison: Agar w1 ka character alien order mein baad mein aata hai
                    if ordToind[w1[j]] > ordToind[w2[j]]:
                        return False
                    # Agar order sahi hai (w1[j] < w2[j]), toh is pair ka faisla ho gaya!
                    # Loop se break karo taaki agle word pair ko compare kiya ja sake.
                    break
            else:
                # Python Magic: Yeh 'else' block tabhi chalta hai jab upar waala 'for' loop 
                # bina kisi 'break' ke successfully poora complete ho jaye (Yani saare characters match ho gaye).
                # Agar saare characters match ho gaye aur w1 ki length w2 se badi hai (e.g., "apple" vs "app"),
                # toh yeh ek invalid sorted order hai, immediately False return karo!
                if len(w1) > len(w2):
                    return False
        
        return True