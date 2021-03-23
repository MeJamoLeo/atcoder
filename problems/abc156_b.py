N, K = map(int, input().split())
count = 0

while N > K:
	N :int = N / K
	count += 1

count += 1
print(count)