A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))

A = [A1,A2,A3]
N = int(input())
B = []
for i in range(N):
	B.append(int(input()))
	for x in range(3):
		for y in range(3):
			if A[x][y] == B[i]:
				A[x][y] = '○'

for i in range(3):
	# 横
	if A[i][0] == A[i][1] == A[i][2]:
		print("Yes")
		exit()
	# 縦
	if A[0][i] == A[1][i] == A[2][i]:
		print("Yes")
		exit()

# 斜め(左to右)
if A[0][0] == A[1][1] == A[2][2]:
	print("Yes")
	exit()
# 斜め(左to右)
if A[0][2] == A[1][1] == A[2][0]:
	print("Yes")
	exit()

print("No")