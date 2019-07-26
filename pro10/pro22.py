p=int(input())
pu=list(map(int,input().split()))[:p]
ri=sum(pu[0:p:2])
ak=sum(pu[1:p:2])
if ri>ak:
  print(ri)
else:
  print(ak)
