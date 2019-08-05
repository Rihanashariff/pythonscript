m=int(input())
r=list(map(int,input().split()))
p=[1]*m
for q in range(m):
    if (q==0):
        if (r[q]>r[q+1]):
            p[q]=p[q]+p[q+1]
    elif (q>0):
        if( r[q] > r[q-1]):
            p[q]=p[q]+p[q-1]
print(sum(p))
