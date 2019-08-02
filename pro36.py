X=int(input())
lst=list(map(int,input().split()))
m=0
for i in range(0,len(lst)-2):
    for j in range(i+1,len(lst)-1):
        for k in range(j+1,len(lst)):
            if lst[i]>lst[j] and lst[j]>lst[k]:
                m=m+1
print(m)
