n1 = int(input())
a3 = list(map(int,input().split()))
c1 = 0
for i in range(0,len(a3)-2):
  for j in range(i+1,len(a3)-1):
    for k in range(j+1,len(a3)):
      if i<j<k and a3[i]>a3[j]>a3[k]:
        c1 = c1+1
print(c1)
