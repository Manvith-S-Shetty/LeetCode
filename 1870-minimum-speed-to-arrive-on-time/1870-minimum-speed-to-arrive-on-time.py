class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour<=len(dist)-1:
            return -1
        left=1
        right=10**7
        while left<right:
            mid=left+(right-left)//2
            time=0
            #mintime=float('inf')
            for i in range(len(dist)):
                current=dist[i]/mid
                if i!=len(dist)-1 and not current.is_integer():
                        current=math.ceil(current)
                time+=current
                
            
            if time<=hour:
                right=mid
                
            else:
                left=mid+1
        return right
                