r,m=map(int,input().split())
l1=list(map(int,input().split()))
l1.sort(reverse=True)
c=0
for i in range(0,len(l1)):
	if m>=l1[i]:
	    s=m//l1[i]
	    c=c+s
	k=m%l1[i]
	if k==0:
		break
print(c)
#s
