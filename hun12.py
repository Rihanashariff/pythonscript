m,r=map(int,input().split())
l1=[int(i) for i in input().split()]
while r>1:
  t=max(l1)
  l1.remove(t)
  r=r-1
print(max(l1))
