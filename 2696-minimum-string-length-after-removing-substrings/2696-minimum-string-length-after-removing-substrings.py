class Solution:
    def minLength(self, s: str) -> int:
        st =[]
        i = 0
        for ch in s:
            
            if st and (st[-1] + ch == "AB" or st[-1] + ch ==  "CD"):
                st.pop()
                i+=1
            else:
                st.append(ch)
        return len(st)