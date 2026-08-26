class Solution:
    def makeGood(self, s: str) -> str:
        st = []
       
        for ch in s:
            if st and st[-1] != ch and ch.lower() == st[-1].lower():
                st.pop()
            else:
                st.append(ch)
        return "".join(st)