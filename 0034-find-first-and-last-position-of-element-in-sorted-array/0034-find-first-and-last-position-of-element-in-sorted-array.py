class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        first=-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                first=mid
                r=mid -1
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        if first == -1:
            return [-1,-1]
        #last part
        last=-1
        #n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                last=mid
                l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:r=mid-1
        return [first,last]
        