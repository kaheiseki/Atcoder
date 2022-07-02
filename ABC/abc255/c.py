x,a,d,n = map(int,input().split())

if d > 0:

  if a + d * (n - 1) < x :
    print(x -  (a + d * (n -1 )))
  elif x < a:
    print(a-x)
  elif d == 0:
    print(abs(a - x))
  else:
    tmp = 0
    for i in range(d):
      if (x + i  - a) % d == 0:
        tmp = i
    print(min(tmp,d - tmp))

else:
  d = -d
  a = -a 
  x = -x
  if a + d * (n - 1) < x :
    print(x -  (a + d * (n - 1)))
  elif x < a:
    print(a-x)
  elif d == 0:
    print(abs(a - x))
  else:
    tmp = 0
    for i in range(d):
      if (x + i  - a) % d == 0:
        tmp = i
    print(min(tmp,d - tmp))