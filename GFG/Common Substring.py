def lcs_of_three(x , y , z):
    m , n , o = len(x) , len(y) , len(z)

    dp=[[[0] * (o+1) for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1 , n+1):
            for k in range(1 , o+1):
                if x[i-1]== y[j-1] ==z[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1]+1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k] , dp[i][j-1][k] , dp[i][j][k-1])

    return dp[m][n][o]



X = "abcde"
Y = "ace"
Z = "ade"

X = "geeks"
Y = "geeksfor"
Z = "geeksforgeeks"
print("Length of LCS:", lcs_of_three(X, Y, Z))


def lcs_oftwo(x , y):
    a , b=len(x) , len(y)

    dp = [[0] * (b + 1) for _ in range(a + 1)]
    for i in range(1 ,a+1):
        for j in range(1 ,b+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i-1][j] , dp[i][j-1])
    return dp[a][b]

# Example usage
X = "abcde"
Y = "ace"
print("Length of LCS:", lcs_oftwo(X, Y))