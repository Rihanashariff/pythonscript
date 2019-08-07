r=int(input())
r1=list(map(int,input().split()))
p=max(r1)
x,y=0,0
for i in range(0,len(r1)-1):
  for j in range(i+1,len(r1)):
    if abs(r1[i]+r1[j])<p:
      x,y=r1[i],r1[j]
      p=abs(x+y)
print(x,y)
