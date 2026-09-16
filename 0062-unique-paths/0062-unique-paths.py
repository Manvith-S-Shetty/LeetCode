class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #using dp
        #dp=[[0]*n for _ in range(m)]
        #dp[0][0]
        #for r in range(1,m):
            #dp[r][0] = 1
        #for c in range(1,n):
            #dp[0][c] = 1
       # for r in range(1,m):
        #    for c in range(1,n):
             #   dp[r][c] = dp[r-1][c] + dp[r][c-1]
        #return dp[m-1][n-1]
        memo={}
        def path(r,c):
            if r>=m or c>=n:
                return 0
            if r ==m-1 and c== n-1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = path(r + 1, c) + path(r, c + 1)

            return memo[(r, c)]
        return path(0,0)

        