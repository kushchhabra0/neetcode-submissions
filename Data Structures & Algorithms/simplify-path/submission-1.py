class Solution:
    def simplifyPath(self, path: str) -> str:
        st = []
        # Path ko '/' ke basis par split karo.
        # Example: "/a/./b/../../c/" -> ["", "a", ".", "b", "..", "..", "c", ""]
        paths = path.split("/")

        for cur in paths:
            # Case 1: Parent Directory ("..")
            # Clear parent folder par wapas jane ke liye stack se top element ko pop karo (agar stack empty na ho)
            if cur == "..":
                if st:
                    st.pop()
            # Case 2: Valid Folder Name
            # Ignore Empty Strings ("" due to extra slashes) and Current Directory (".")
            elif cur != "" and cur != ".":
                st.append(cur)
        
        # Step 3: Canonical path construct karo root '/' se start karke elements ko '/' se jodte huye
        return "/" + "/".join(st)