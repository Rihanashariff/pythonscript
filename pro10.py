a2=int(input())
c1=list(map(int,input().split()))
b=0
for m in range(0,a2):
	for p in range(0,m):
		if c1[p]<c1[m]:
			b=b+c1[p]
print(b)
