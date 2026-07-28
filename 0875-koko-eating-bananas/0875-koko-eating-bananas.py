
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1 # to start with the 1st one
        r=max(piles) # maximum element present in the pile
        while l<r:
            mid=(l+r)//2
            hr=0
            for p in piles:
                hr+=math.ceil(p/mid) #ceil fro roundup
            if hr<=h:
                r=mid
            else:
                l=mid+1 #returning so +1
        return l