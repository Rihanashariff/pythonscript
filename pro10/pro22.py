p=int(input())
pu=list(map(int,input().split()))[:y]
ri=sum(pu[0:y:2])
ak=sum(pu[1:y:2])
if ri>ak:
  print(ri)
else:
  print(ak)
