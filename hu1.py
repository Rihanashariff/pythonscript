try:
	n=int(input())
	array=list(map(int,input().split()))
	pk=[]
	for i in array:
		if array.count(i)>1:
			if i not in pk:
				pk.append(i)
	print(*pk)
	if len(pk)==0:
		print("unique")
except ValueError:
	print("invalid")
