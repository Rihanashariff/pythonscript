n=int(input())
ls=input().split(" ")
ls=[int(n) for n in ls]
final=[]
for k in range(0,n):
  if(k==ls[k]):
    final.append(ls[k])
if not(len(final)==0):
  final=sorted(final)
  for i in range(0,len(final)):
    print(final[i],end=' ')
else:
  print("-1")
