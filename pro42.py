n1,k2=map(int,input().split())
l3=list(map(int,input().split()))
if k2==1:
    print(min(l3))
elif k2==2:
    print(max(l3[0],l3[n1-1]))
else:
    print(max(l3))
