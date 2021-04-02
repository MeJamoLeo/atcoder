N = int(input())
l = list(map(int, input().split()))

for i in range(N):
	if l[i] % 2 == 0 and l[i] % 3 != 0 and l[i] % 5 != 0:
		print("DENIED")
		exit()
print("APPROVED")
