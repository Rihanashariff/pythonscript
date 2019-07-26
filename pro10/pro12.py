pu,ri = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(ri):
  p,s = map(int, input().split())
  print(min(lst[p-1:s]))
