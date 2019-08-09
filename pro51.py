n1=int(input())
l2=list(map(int,input().split()))
t1=[]
c2=1
for i in range(n1):
	for j in range(i,n1):
		if j==n1-1:
			break
		if (l2[j]>0 and l2[j+1]<0) or (l2[j]<0 and l2[j+1]>0):
			c2=c2+1
		else:
			break
	t1.append(c2)
	c2=1
print(*t1)
