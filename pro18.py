p,r=map(int,input().split())
l2=[]
ri=0
for i in range(p):
    l2.append(list(map(int,input().split())))   
for i in range(p):
    for j in range(r-1):
        for k in range(j+1,r+1):
            if l2[i][j:k]==[1]*len(l2[i][j:k]):
                 if all(l2[p+i][j:k]==[1]*len(l2[p+i][j:k]) for p in range(len(l2[i][j:k])-1)):
                     if len(l2[i][j:k])>ri:
                        ui=len(l2[i][j:k])
if len(l2)==1 and len(l2[0])==1 and l2[0][0]==1:
    print(1)
for i in range(ri):
    print(*[1]*ri) 
