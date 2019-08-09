n1,k1=map(int,input().split())
l2=[]
c3=0
for i in range(n1):
    l2.append(input())
for i in range(n1):
    for j in range(k1-1):
        if l2[i][j]=="R" and l2[i][j+1]=="R":
            c3=c3+5
        elif l2[i][j]=="G" and l2[i][j+1]=="G":
            c3=c3+3
print(c3)
