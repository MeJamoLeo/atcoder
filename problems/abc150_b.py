N = int(input())
S = input()
S = list(S)

count = 0

for i in range(N):
	if S[i-2] == "A" and S[i-1] == "B" and S[i] == "C":
		count += 1

print(count)
