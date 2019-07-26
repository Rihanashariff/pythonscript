y,sar = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(sar):
  yuv,sara = map(int, input().split())
  print(min(lst[yuv-1:sara]))
