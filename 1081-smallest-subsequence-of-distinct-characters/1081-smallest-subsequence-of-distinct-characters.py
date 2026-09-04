from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        st = []
        count = Counter(s)
        for ch in s:
            count[ch] -= 1
            if ch in st:
                continue 
            while st and st[-1]>ch and count[st[-1]]>0:
                st.pop()
            st.append(ch)
        res = ''.join(st)
        return res