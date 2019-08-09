n1,k1 = map(int,input().split())
l3 = list(map(int,input().split()))
c2= 0
for i in l3:
    if(i+k1 <=5):
        c2+=1
h=c2//3
print(h)
