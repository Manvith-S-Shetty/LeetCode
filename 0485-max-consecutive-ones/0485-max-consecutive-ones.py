class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        max_c=0
        for num in nums:
            if num==1:
                count+=1
                max_c=max(max_c,count)
            else:
                count=0
        return max_c

      