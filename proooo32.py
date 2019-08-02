m,r=map(int,input().split())
if m>r:
    p,k=r,m
lst=[]
for i in range(m):
    lst1=list(map(int,input().split()))
    lst1.sort()
    lst.append(lst1)
for j in range(0,k):
    lst2=[]
    for i in range(0,m):
        lst2.append(lst[i][j])
    lst2.sort()
    x=0
    for i in range(0,m):
        lst[i][j]=lst2[x]
        x=x+1
for i in lst:
    print(*i)




  
