class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_prefix = [0]*n  #creates an array of n zeros.
        max_suffix = [0]*n #creates an array of n zeros.

        max_prefix [0] = nums[0] # assigning the 1st value to the max_prefix
        for i in  range(1,n):
            max_prefix[i] = max(max_prefix[i-1],nums[i])

        max_suffix[n-1] = nums[n-1] #assigning last value to the max_suffix 
        for i in range(n-2,-1,-1) : #Start from index 2 and move backwards until index 0.
            max_suffix[i] = min(max_suffix[i+1],nums[i])
        
        for i in range(n):
            score = max_prefix[i] - max_suffix[i]
            if score <= k:
                return i #it return the actual index
        return -1