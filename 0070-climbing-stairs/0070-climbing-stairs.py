class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for k in range(3, n+1):
            if dp[k] < 1:
                dp[k] = dp[k-2] + dp[k-1]
        
        return dp[n]