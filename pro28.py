r=int(input())
l1=list(map(int,input().split()))
l1.sort()
p=0
d=0
for i in range(len(l1)):
    if l1[i]>=p:
        d=d+1
    p=p+l1[i]
print(d)
