class Solution:
    def calculate(self, s: str) -> int:
        st = []
        num =0
        op ="+"
        res = 0
        for ch in s:
            if ch.isdigit():
                num = num*10+int(ch)
            elif ch in "+-":
                if op =="+":
                    res += num
                else:
                    res -= num
                op = ch
                num = 0

            elif ch =="(":

                st.append((res,op))
                res = 0
                op="+"
                num = 0
            elif ch == ")":
                if op =="+":
                    res += num
                else:
                    res -= num
                prev,prev_op = st.pop()

                if prev_op == "+":
                    res = prev + res
                else:
                    res = prev - res 
                op = "+"
                num = 0

        if op =="+":
            res +=num
        else:
            res -=num
        return res

