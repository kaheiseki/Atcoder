n,m,k = map(int,input().split())

a = m * n

b = a - k 

c = b + n - 1
 
M =998244353 

dp = [[] * k] * n
for i in range(n):
  if i == 0 and i <= m:

    for j in range(k):
      # if j == 0:
        dp[i][j] = 1
  else:
   for j in range(k):
      if j == 0:
        dp[i][j] = 1

print(dp)