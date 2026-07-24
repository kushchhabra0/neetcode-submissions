class Solution:
    def decodeString(self, s: str) -> str:
        string_st = []
        count_st = []
        res = ""
        k = 0

        for c in s:
            if c.isdigit():
                k = k*10 + int(c)
            elif c == '[':
                string_st.append(res)
                count_st.append(k)
                res = ""
                k = 0
            elif c == ']':
                temp = res
                res = string_st.pop()
                count = count_st.pop()
                res = res + temp*count
            else:
                res = res + c
        return res