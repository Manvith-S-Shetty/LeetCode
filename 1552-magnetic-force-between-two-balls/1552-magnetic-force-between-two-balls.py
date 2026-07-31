class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def can(place):
            ball=1
            length=position[0]
            for i in range(1,len(position)):
                if position[i]-length>=place:
                    ball+=1
                    length=position[i]
            return ball>=m
        left=1
        right=position[-1]-position[0]
        while left<=right:
            mid=left+(right-left)//2
            if can(mid):
                left=mid+1
            else:
                right=mid-1
        return right