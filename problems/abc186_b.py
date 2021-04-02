H, W = map(int, input().split())
board = []
min_n = 100
ans = 0

for i in range(H):
	board.append(list(map(int, input().split())))
	if min_n > min(board[i]):
		min_n = min(board[i])

for i in range(H):
	for j in range(len(board[i])):
		ans += board[i][j] - min_n

print(ans)