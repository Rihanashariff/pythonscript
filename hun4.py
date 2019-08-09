n1=int(input())
l1=[int(x) for x in input().split()]
for i in range(len(l1)):
     if l1.count(l1[i])==1:
          print(l1[i])
