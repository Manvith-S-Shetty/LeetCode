class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = min(nums)
        max_val = max(nums)

        missing = (set(range(min_val,max_val+1)))-set(nums)
        return sorted(list(missing))
        