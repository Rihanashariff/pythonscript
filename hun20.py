a2,b2=map(int,input().split())
l2=[]
e=0
k1=[]
for i in range(a2,b2+1):
        l2.append(bin(i)[2::])
for i in range(0,len(l2)):
        k1.append(l2[i].count("1"))

for i in range(0,len(k1)):
        if k1[i]!=1 and k1[i]!=2:
                for p in range(2,k1[i]):
                        if k1[i]%p==0:
                                break
                if p==k1[i]-1:
                        e=e+1
        elif k1[i]==2:
                e=e+1
print(e)
