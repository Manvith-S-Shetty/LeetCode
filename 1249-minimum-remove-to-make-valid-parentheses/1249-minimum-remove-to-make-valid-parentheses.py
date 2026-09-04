class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        ans = list(s)# it contain all the list of the things present in the s
        for i,ch in enumerate (s):
            if ch == '(':
                st.append(i) # here I use the index if you want to use the char itself then you need to chnage in --1
            elif ch ==')':
                if st:
                    
                    st.pop()
                else:
                    ans[i] = ''
        while st: #--change here like  for loop for each char in st take their index and make " "
            i = st.pop()
            ans[i] = ''
        return "".join(ans)