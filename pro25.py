r=int(input())
l1=list(map(int,input().split()))
m=[]
k=1
for i in range(r-1):
	if l1[i]<l1[i+1]:
		k+=1
	else:
		m.append(k)
		k=1
m.append(k)
print(max(m))
