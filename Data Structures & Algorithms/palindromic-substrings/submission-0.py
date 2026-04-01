class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        count = 0

        #base case:
        for i in range(n):
            dp[i][i] = True
            count += 1

        #base case 2nd for 2 character length
        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                count += 1

        for L in range(3,n+1):
            for i in range(n-L+1):
                j = i + L - 1
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    count += 1
        return count



        
        
        