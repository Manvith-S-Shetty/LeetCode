class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
       
        def solve(left,right):
            if left==right:
                return nums[left]
            player1=nums[left]-solve(left+1,right)
            player2=nums[right]-solve(left,right-1)
            return max(player1,player2)
        return (solve(0,len(nums)-1))>=0
