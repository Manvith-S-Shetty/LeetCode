class Solution:
    def reverse(self, x: int) -> int:
        #n=len(str(abs(x)))
        sign = -1 if x<0 else 1 #check if the value has - or + 

        rev = int(str(abs(x))[::-1]) #reverse it
        res = sign*rev

        if res<-2**31 or res > 2**31-1:
            return 0
        return res #multiply with the sign (+/-)