import math


n,k = map(int,input().split())

a = list(map(int,input().split()))
xy = []
have = []
dont = []

for i in range(n):
  tmp = list(map(int,input().split()))
  if i+1 in a:
    xy.append(tmp)
    have.append(tmp)
  else:
    xy.append(tmp)
    dont.append(tmp)
mx_a = 0

for i in dont:
  mn = 10000000
  for j in have:
    if math.sqrt((i[0]-j[0])**2 + (i[1]-j[1])**2) < mn:
      mn =math.sqrt((i[0] - j[0]) **2 + (i[1] - j[1]) ** 2)
  if mx_a < mn:
    mx_a = mn
print(mx_a)