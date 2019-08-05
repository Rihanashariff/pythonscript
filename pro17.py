r,m=map(int,input().split())
p=list(map(int,input().split()))[:r]
coun=0
for c in range(0,len(p)-1):
  for sd in range(c+1,len(p)-1):
    if(p[c]+p[sd]==m):
      coun+=1  
if (coun==1):
  print("yes")
else:
  print("no")
