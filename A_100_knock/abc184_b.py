N, X = map(int, input().split())
S = list(input())
for char in S:
	if char == 'o':
		X += 1
	else:
		if X > 0:
			X -= 1
print(X)