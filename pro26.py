r=int(input())
l2=list(map(int,input().split()))
k=[]
t=1
for i in l2:
    if i not in k:
        k.append(i)
        
        
for i in range(len(k)-1):
	if k[i]<k[i+1]:
		t+=1
print(t)
