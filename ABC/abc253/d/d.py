from distutils.command.bdist_msi import bdist_msi


n,a,b = map(int,input().split())

am = a - n % a
bm = b - n % b
print(am,bm)