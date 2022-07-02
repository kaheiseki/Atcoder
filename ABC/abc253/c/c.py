import heapq

q = int(input())
A = {}
BMIN = []
BMAX = []

heapq.heapify(BMIN)
heapq.heapify(BMAX)
mn = 1000000000
mx = 0

for i in range(q):
  s = list(input().split())
  if s[0] == "1":
    if s[1] not in A:
      A[s[1]] = 1
      mn = min(mn,int(s[1]))
      mx = max(mx,int(s[1]))
    else:
      A[s[1]] += 1
  if s[0] == "2":
    if s[1] in A:
      d = A[s[1]]
      discount = min(int(s[2]),d)
      A[s[1]] -= discount
      if A[s[1]] == 0:
        A.pop(s[1])
        if mn == s[1]:
          print(list(A.keys()))
        if mx == s[1]:
          print(list(A.keys()))

  if s[0] == "3":
    l = list(A.keys())
    print(mx-mn)
