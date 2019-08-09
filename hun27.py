a1=input()
a2=list(a1)
if a2==a2[::-1]:
	while a2==a2[::-1]:
		a2[-1]=""
g=""
for i in a2:
	g=g+i
print(g)
