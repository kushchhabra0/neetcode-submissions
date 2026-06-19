class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        
        # Phone keypad ki digit-to-character mapping
        digitTochar = {
            "2": "abc",  "3": "def",  "4": "ghi",
            "5": "jkl",  "6": "mno",  "7": "pqrs",
            "8": "tuv",  "9": "wxyz"
        }

        def backtrack(i, curstr):
            # Base Case: Agar current string ki length input digits ke barabar ho gayi,
            # matlab ek valid combination poori ban chuki hai!
            if len(curstr) == len(digits):
                res.append(curstr)
                return
            
            # Current digit ke saare mapped characters par loop chalao
            for c in digitTochar[digits[i]]:
                # Python strings are immutable, so 'curstr + c' automatically 
                # creates a new copy for the next frame, making explicit backtracking (.pop()) unnecessary.
                backtrack(i + 1, curstr + c)
        
        # Edge Case: Agar input string khaali ("") hai, toh seedhe empty list return karo
        if digits:
            backtrack(0, "")
            
        return res