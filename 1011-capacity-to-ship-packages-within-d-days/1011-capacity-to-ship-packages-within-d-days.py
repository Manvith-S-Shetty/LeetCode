class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # for capacity in range(max(weights),sum(weights)+1):
        # dayuse=1
        # currentcapacity=0
        #     for weight in weights:
        #         if currentcapacity+weight<=capacity:
        #             currentcapacity+=weight
        #         else:
        #             dayuse+=1
        #             currentcapacity=weight
        #     if dayuse<=days:
        #         return capacity
        left=max(weights)
        right=sum(weights)
        while left<right:
            mid=(left+right)//2
            dayuse=1
            currentcapacity=0
            for w in weights:
                if currentcapacity+w<=mid:
                    currentcapacity+=w
                else:
                    dayuse+=1
                    currentcapacity=w
            if dayuse<=days:
                right=mid
            else:
                left=mid+1
        return left