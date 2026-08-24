class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
    
        def track(string):
            st = []
            for ch in string:
                if ch == '#':
                    if st :
                        st.pop()
                else:
                    st.append(ch)
            return ''.join(st)
        return track(s) == track(t)