N, W = map(int, input().split())

count = 0
while N >= W * count:
	count += 1
print(count - 1)
