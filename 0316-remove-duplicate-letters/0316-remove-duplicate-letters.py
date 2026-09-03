'''
THE KEY OF THIS PROBLEM IS SIMPLE JUST DO THE CONDITION LIKE
IF STACK PRESENT OR NOT AND 
TOP ELEMENT OF STACK IS GREATER TO THE CURRENT ELEMENT OR NOT
CAN WE REMOVE SAFELY MEANS THE COUNT IS 0 OR NOT BCZ THE ELEMENT ONLY APPEARS ONCE ONLY
'''
from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        st =[]
        for ch in s:
            count[ch] -=1 #WE NEED TO DECREASE THE COUNT VALUE OF EACH CHAR WE SAR
            if ch in st: #WHAT IT DOES IS IF THE ELEMENT REPEATED IT IGNORE IT
                continue
            while st and st[-1]>ch and count[st[-1]]>0: 
                st.pop()
                
            st.append(ch)
        res = "".join(st) #THE STACK GIVE [""] OUTPUT SO CONVERT TO STRING
        return res