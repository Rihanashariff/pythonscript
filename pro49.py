s1=input()
t1=input()
c1=1
n2=len(s1)
for i in range(0,len(t1)-n2,n2):
	if t1[i:i+n2]==s1:
		c1=c1+1
print(c1)
