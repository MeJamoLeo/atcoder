N = int(input())
X = list(map(int, input().split()))

ans = 1000000000000000

for i in range(100):
	tmp = 0
	for j in range(len(X)):
		tmp += (X[j] - i) * (X[j] - i)
	if tmp < ans:
		ans = tmp

print(ans)
