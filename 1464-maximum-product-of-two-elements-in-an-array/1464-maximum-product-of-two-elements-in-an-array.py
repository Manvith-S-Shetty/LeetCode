class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#         maxi=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 product=(nums[i]-1)*(nums[j]-1)
#                 maxi= max(maxi,product)
#         return maxi
            largest=second=0
            for num in nums:
                if num>largest:
                    second=largest
                    largest=num
                elif num > second:
                    second=num
            return (largest-1)*(second-1)