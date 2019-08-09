r,k1=map(int,input().split())
e=[]
for i in range(r):
	s=set(map(int,input().split()))
	e.append(s)
c2=s.intersection(*e)
print(*c2)
