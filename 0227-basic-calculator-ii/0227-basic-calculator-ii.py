class Solution:
    def calculate(self, s: str) -> int:
        st = []
        num = 0
        op ="+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num*10+ int(ch)
            if ch in "+-*/" or i == len(s)-1:
                if op == '+':
                    st.append(num)
                if op == '-':
                    st.append(-num)
                if op == '*':
                    st.append(st.pop()*num)
                if op == '/':
                    st.append(int(st.pop()/num))
                op = ch
                num = 0
        return sum(st)