m=int(input())
l4=[]
for i in range(1,m):
    rev=0
    temp=i
    while temp!=0:
        re=temp%10
        rev=rev+re
        temp=temp//10
    if i+rev==m:
        l4.append(i)
print(len(l4))
for j in range(0,len(l4)):
    print(l4[j])
