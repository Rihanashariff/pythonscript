r=int(input())
m,p=[],[]
for i in range(0,r):
  b=sorted(list(map(int,input().split())))
  p=p+m
print(*sorted(p))
