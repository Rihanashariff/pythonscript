k=int(input(""))
temp=k
p=0
while(k>0):
    x=k%10
    p=p*10+x
    k=k//10
if(temp==p):
    print("yes")
else:
    print("no")
