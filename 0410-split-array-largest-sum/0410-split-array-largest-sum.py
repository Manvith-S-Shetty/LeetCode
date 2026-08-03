class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right = max(nums),sum(nums)
        while left <= right:
            mid = left+(right-left)//2
            if self.cansplit(nums,k,mid):
                ans = mid
                right =mid-1
            else:left = mid+1
        return ans
    def cansplit(self,nums,k,mixs):
        count = 1
        currSum = 0
        for n in nums:
            if currSum+n <= mixs:
                currSum += n
            else:
                count +=1
                currSum =n
        return count <=k