class Solution:
    def decodeString(self, s: str) -> str:
        st =[]
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num*10+int(ch)
            elif ch == "[":
                st.append((curr,num))
                curr = ""
                num = 0
            elif ch == "]":
                prev,repeat = st.pop()
                curr = prev+repeat*curr
            else:
                curr += ch
        return curr