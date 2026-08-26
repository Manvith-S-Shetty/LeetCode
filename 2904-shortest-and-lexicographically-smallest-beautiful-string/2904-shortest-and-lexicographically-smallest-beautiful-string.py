class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
        for i in range(len(s)): # 1st find the positions of 1 in the given string
            
            if s[i] == "1":
                ones.append(i)

        if len(ones)<k: #if the given k in greater that 1's present in  the s then ""
            return ""
            
        ans = ""

        for i in range(len(ones)-k+1): # iterate through the position of 1 in the []
            start = ones[i] 
            end = ones[i+k-1]
            cand = s[start:end+1] #range of the positions of ones in the given string
            
            if ans == "": #initial assigning the value to the ans
                ans = cand
            
            elif len(cand)<len(ans): #we needed the smaller one
                ans = cand
            
            elif len(cand) == len(ans) and cand<ans: #even though the len same but the value is if graeter for ans then swap
                ans = cand
        
        return ans
