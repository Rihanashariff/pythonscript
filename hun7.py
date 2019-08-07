r=int(input())
p=[int(x) for x in input().split()]
l2=[]

for i in range(0,len(p)):
    if  i %2!=0 and p[i]%2==0:
        l2.insert(i,p[i])
    elif i%2==0 and p[i]%2!=0:
        l2.insert(i,p[i])

for i in range(0,len(l2)-1):
    print(l2[i], end=" ")
print(l2[-1])   


