N, K, M = map(int, input().split())

A = map(int, input().split())

goal_total_point = M * N

corrent_total = 0
for a in A:
	corrent_total += a

res = goal_total_point - corrent_total
if 0 <= res <= K:
	print(res)
elif res < 0:
	print(0)
else:
	print(-1)