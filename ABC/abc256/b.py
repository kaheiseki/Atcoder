n = int(input())
a = list(map(int,input().split()))

b = [0,0,0]

answer = 0
for i in range(n):
  if a[i] == 1:
    answer += b[2:].count(1)
    b = [1] + b[0:2]

  elif a[i] == 2:
    answer += b[1:].count(1)
    b = [0,1] + b[0:1]

  elif a[i] == 3:
    answer += b.count(1)
    b = [0,0,1]

  elif a[i] == 4:
    answer += b.count(1) + 1
    b = [0,0,0]
print(answer)