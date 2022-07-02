import copy

n = int(input())

sl = []
tl = []
a = "Yes"

for i in range(n):
  s,t = input().split()
  sl.append(s)
  tl.append(t)

for i in range(n):
  s = sl[i]
  t = tl[i]
  tmps = copy.copy(sl)
  tmps.remove(s)
  tmpt = copy.copy(tl)
  tmpt.remove(t)
  print(tmpt)
  if (s in tmps and t in tmpt) or (s in tmpt and t in tmps):
    a = "No"
    break
print(a)
    