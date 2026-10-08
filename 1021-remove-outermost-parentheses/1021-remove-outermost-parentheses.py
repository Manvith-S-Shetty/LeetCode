class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open = 0
        ans = ""
        for ch in s:
            if ch == "(":
                open +=1
                if open == 1:
                    continue
            else:
                open -=1
                if open == 0:
                    continue
            ans +=ch
        return ans