n1=int(input())
array=list(map(int,input().split()))
p2=1
op=[]
for i in array:
  p2=p2*i
for i in array:
  op.append(p2//i)
print(*op)
