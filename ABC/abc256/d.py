n = int(input())

R = []
for i in range(n):
  l,r = map(int,input().split())
  R.append(l,r)
R.sort()

ans = 0
con_r = R[0][1]

for i in range(n):
  if con_r < R[i][0]:
    ans += 1
    con_r = R[i][1]
  else:
    con_r = max(con_r,R[i][1])

print(ans)
