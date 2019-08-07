m,q=map(int,input().split())
a=list(map(int,input().split()))
d=list(map(int,input().split()))
r=[]
s=0
for i in range(m):
    z=d[i]/a[i]
    r.append(z)
while q>=0 and len(r)>0:
    mindex=r.index(max(r))
    if q>=a[mindex]:
        s=s+d[mindex]
        q=q-a[mindex]
    a.pop(mindex)
    d.pop(mindex)
    r.pop(mindex)
print(s)
