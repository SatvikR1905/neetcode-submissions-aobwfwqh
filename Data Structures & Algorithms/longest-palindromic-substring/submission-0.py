class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        start = 0
        max_len = 1

        #base case 1 : for single character
        for i in range(n):
            dp[i][i] = True

        #base case 2 : for 2 characters
        for i in range(n-1):
            dp[i][i+1] = s[i] == s[i+1]
            if dp[i][i+1]:
                start = i
                max_len = 2

        for L in range(3,n+1):
            for i in range(n-L+1):
                j = i + L - 1
                dp[i][j] = s[i] == s[j] and dp[i+1][j-1]
                if dp[i][j] and L > max_len:
                    start = i
                    max_len = L

        return s[start : start + max_len]

        
        