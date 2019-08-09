from itertools import permutations
r=input()
m=permutations(r)
for j in list(m):
	print(''.join(j))
