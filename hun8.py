r=int(input())
l3=[int(x) for x in input().split()]
p=[]
for i in range(0,len(l3)):
	for j in range(i+1,len(l3)):
		for k in range(j+1,len(l3)):
			if l3[i]+l3[j]==l3[k]:
				p.append(l3[k])
				print(l3[i],l3[j],l3[k])
				break
