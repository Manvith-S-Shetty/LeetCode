class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res = 0
        min_index = [0]*len(nums)
        max_index = [0]*len(nums)
        max_index[0] = nums[0]
        for i in range (1,len(nums)):
            max_index[i] = max(max_index[i-1],nums[i])
        min_index[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            min_index[i] = min(nums[i],min_index[i+1])
        for i in range(len(nums)):
            score = max_index[i] - min_index[i]
            if score <= k:
                return i #it return the actual index
        return -1
        