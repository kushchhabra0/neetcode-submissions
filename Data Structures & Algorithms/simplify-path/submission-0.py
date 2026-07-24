class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        paths = path.split("/")

        for cur in paths:
            if cur == "..":
                if st:
                    st.pop()
            elif cur != "" and cur != '.':
                st.append(cur)
        
        return "/" + "/".join(st)