r=int(input())
l2=[int(x) for x in input().split()]
l3=[]
d=0
for i in range(0,len(l2)):
    for j in range(i+1,len(l2)):
        if l2[i]==l2[j]:
            l3.append(l2[i])
            
for  i in range(0,len(l3)-1):
    d=d+1
    print(l3[0])
if d==0:
    print("unique")
