n1=int(input())
l1=list(map(int,input().split()))
a1_has=0
b1_has=0
l1.sort(reverse=True)
for i in l1:
  s2=a1_has+i
  if b1_has>s2:
    a1_has=s2
  else:
    a1_has=b1_has
    b1_has=s2
print(a1_has,b1_has)
