class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        for x in nums1:
            if x % 2 ==1:
                min_odd = min(x,min_odd)
        if min_odd == float('inf'): #THIS IS BCZ OF THEIR IS NO ELMENT IS ODD 
                return True
        for x in nums1:
            if x % 2 == 0 and x<min_odd:
                return False
        return True