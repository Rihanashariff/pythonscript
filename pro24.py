k=int(input())
m=2**k
ar=[]
for i in range(0,m):
    l=bin(i)[2:].zfill(k)
    if(len(l)<len(bin(2**k-1)[2:])):
        ar.append([l.count("1"),l])
    else:
        ar.append([l.count("1"),l])
ar.sort()
for i in range(len(ar)):
    print(ar[i][1])
