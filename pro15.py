r=int(input())
p=list(map(int,input().split()))
ll=[]
for i in p:
  m=bin(i)
  ll.append(m)
k=sorted(ll)
k.reverse()
for j in k:
  print(int(j,2))
