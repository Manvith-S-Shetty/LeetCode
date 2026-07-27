from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans=window=0
        freq=defaultdict(int)
        #for making the sum of 1st k
        for i in range(k):
            window+=nums[i]
            freq[nums[i]]+=1
        if len(freq)==k: #to check the uniqueness
            ans=window
        #for sliding.
        for i in range(k,len(nums)):
            left=nums[i-k]
            window-=left #remove the left elemnt
            freq[left]-=1
            if freq[left]==0:
                del freq[left]
            # adding the new element
            window+=nums[i]
            freq[nums[i]]+=1
        
            if len(freq)==k:
                ans=max(ans,window)
        return ans
        

            