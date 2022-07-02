s = input()
l = [0,1,2,3,4,5,6,7,8,9]

for i in range(9):
  l.remove(int(s[i]))

print(l[0])