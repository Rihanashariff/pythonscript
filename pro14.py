r,m=map(int,input().split())
p=list(map(int,input().split()[:r]))
final=[]
for i in range (m):
    s=list(map(int,input().split())) 
    final.append(s)
for j in final:
    q=0
    for k in range (j[0]-1,j[1]):
        q=q^p[k]
    print(q)
