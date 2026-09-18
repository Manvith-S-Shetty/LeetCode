class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binary(l,r):
            
            if l>r:
                return -1
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if target< nums[mid]:
                return binary(l,mid-1)
            return binary(mid+1,r)
        return binary(0,len(nums)-1)