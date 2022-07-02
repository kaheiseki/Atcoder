n,q = map(int,input().split())

a = list(map(int,input().split()))
min_a = min(a)
tmp = 0
table = [0 for i in range(10 ** 9 + 1)]

for i in range(len(a)):
    tmp += min_a - a[i]
    table[[a[i]]] += 1

sum_table = [0 for i in range(10 ** 9 + 1)]
for i in range(1,10 ** 9 + 1):
  sum_table[i] = sum_table[i-1] - table[i]

print(sum_table[1:11])


for i in range(q):
  ans = tmp
  x = int(input())
  if a[0] - x > 0:
    ans += (min_a - x) * len(a)
  else:
    ans += (x - min_a) * len(a)
  print(ans)