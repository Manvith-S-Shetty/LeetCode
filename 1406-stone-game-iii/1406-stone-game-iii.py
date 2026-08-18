class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] *(n+3)
        for i in range(n - 1, -1, -1):
            res = float("-inf")
            current = 0
            for j in range(1,4):
                if i + j -1 <n:
                    current +=stoneValue[i+j-1]
                    res = max(res,current - dp[i+j])
            dp[i]=res
        if dp[0] > 0:
            return "Alice"
        elif dp[0] <0:
            return "Bob"
        else:
            return "Tie"