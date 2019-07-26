pu,u=map(int,input().split())
lst1=list(map(int,input().split()))
l=[]
for i in range(0,u):
     x,y=map(int,input().split())
     l.append([x,y])
for i in range(u):
     lwr=l[i][0]
     upr=l[i][1]
     p=sum(lst1[lwr-1:upr])
     print(p)
