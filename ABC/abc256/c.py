h_1,h_2,h_3,w_1,w_2,w_3 = map(int,input().split())

l1 = []
count = 0

for i in range(1,29):
  for j in range(1,29 - i):
    for k in range(1,29 - i - j):
      for l in range(1,29):
        for m in range(1,29 - l):
          for n in range(1,29 - l - m):
            if i + j + k == w_1 and l + m + n == w_2:
              a_1 = h_1 - (i + l)
              a_2 = h_2 - (j + m)
              a_3 = h_3 - (k + n)
              if a_1 > 0 and a_2 > 0 and a_3 > 0:
                if a_1 + a_2 + a_3 == w_3:
                  count += 1
                  print(i,j,k,l,m,n,a_1,a_2,a_3)

print(count)


