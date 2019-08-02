ar=input()
m=0
for i in range(0,len(ar)-1):
  for j in range(i+1,len(ar)):
    if ar[i]<ar[j]:
      x=1
      print(ar[j:])
      break
  if x==1:
    break
else:
  print(ar)
