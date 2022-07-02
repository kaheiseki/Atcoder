h,w = map(int,input().split())
a = []

for i in range(h):
  s = input()
  for j in range(w):
    if str(s[j]) == "o":
      a.append([i,j])


if a[1][0] - a[0][0] > 0:
  print(a[1][0] - a[0][0] + a[1][1] - a[0][1])
else:
  print(-a[1][0] + a[0][0] + a[1][1] - a[0][1])