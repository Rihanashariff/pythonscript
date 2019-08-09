r,m=map(int,input().split())
s1= [[abs(i-m),i]for i in [int(x) for x in input().split()]]
s1.sort()
#print(s)
s1=s1[1:]
#print(s)
#print(s[::3])
s1=[i[1] for i in s1[:3]]
print(*s1)
