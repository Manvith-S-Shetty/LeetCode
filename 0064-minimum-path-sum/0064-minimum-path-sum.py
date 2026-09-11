class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # m contain the value of row
        n = len(grid[0]) #n has col vgalue 
        dp = [[0]*n for _ in range(m)] # 0 and 0 element cell in row and clo
        dp[0][0] = grid[0][0] #add the 1st value of grid to the dp 
        #1st row add to the dp
        for r in range(1,m):
            dp[r][0] = dp[r-1][0] + grid[r][0]
        
        #1st col add to the dp

        for c in range(1,n):
            dp[0][c] = dp[0][c-1]+grid[0][c]
    #remaining elemnts
        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = grid[r][c] + min(dp[r-1][c],dp[r][c-1])
        return dp[m-1][n-1]
