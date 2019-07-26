p=int(input())
put=list(map(int,input().split()))
ans=int(y/2)
ri=put[:ans]
sh=put[ans::]
if ((sum(ri)//len(ri))==(sum(sh)//len(sh))):
    print("yes")
else:
    print("no")
