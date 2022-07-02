n = input()

def makes(n):
  if n == 1:
    return "1"
  else:
    return makes(n-1) + n + makes(n-1)

print(makes(n))
